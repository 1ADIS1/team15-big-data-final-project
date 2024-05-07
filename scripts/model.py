from pyspark import keyword_only

from pyspark.ml import Pipeline, Transformer
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.param.shared import HasInputCols, HasOutputCols
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, FloatType

from pyspark.ml.regression import LinearRegression, DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator

import numpy as np


class LatLongToXYZ(Transformer, HasInputCols, HasOutputCols):
    @keyword_only
    def __init__(self, inputCols=None, outputCols=None):
        super(LatLongToXYZ, self).__init__()
        kwargs = self._input_kwargs
        self.setParams(**kwargs)

    def _transform(self, dataset):
        def f(lat, lon, alt=0, in_radians=False):
            if not in_radians:
                lat = np.deg2rad(lat)
                lon = np.deg2rad(lon)
                alt = np.deg2rad(alt)

            A = 6378137  # WGS-84 semi-major axis
            E2 = 6.6943799901377997e-3  # WGS-84 first eccentricity squared
            n = A / np.sqrt(1 - E2 * np.sin(lat) * np.sin(lat))

            x = (n + alt) * np.cos(lat) * np.cos(lon)
            y = (n + alt) * np.cos(lat) * np.sin(lon)
            z = (n * (1 - E2) + alt) * np.sin(lat)

            return [float(x), float(y), float(z)]

        # Define the UDF
        t = ArrayType(FloatType())
        udf_func = udf(f, t)

        # Get the input columns
        in_cols = dataset.select(self.getInputCols()).columns

        # Apply the UDF
        dataset = dataset.withColumn(self.getOutputCols()[0], udf_func(*in_cols)[0])
        dataset = dataset.withColumn(self.getOutputCols()[1], udf_func(*in_cols)[1])
        dataset = dataset.withColumn(self.getOutputCols()[2], udf_func(*in_cols)[2])

        return dataset

    @keyword_only
    def setParams(self, inputCols=None, outputCols=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)


categorical_cols = [
    "manufacturer",
    "car_condition",
    "cylinders",
    "fuel",
    "transmission",
    "car_drive",
    "car_size",
    "car_type",
    "us_state",
    "region_url",
]

numerical_cols = [
    "manufactured_year",
    "odometer",
]


# Add here your team number teamx
team = "team15"

# Location of your Hive database in HDFS
warehouse = "project/hive/warehouse"

spark = (
    SparkSession.builder.appName(f"{team} - spark ML")
    .master("yarn")
    .config("hive.metastore.uris", "thrift://hadoop-02.uni.innopolis.ru:9883")
    .config("spark.sql.warehouse.dir", warehouse)
    .config("spark.sql.avro.compression.codec", "snappy")
    .enableHiveSupport()
    .getOrCreate()
)

# We can also add
# .config("spark.sql.catalogImplementation","hive")\
# But this is the default configuration
# You can switch to Spark Catalog by setting "in-memory" for "spark.sql.catalogImplementation"
spark.sql("SHOW DATABASES").show()
spark.sql("USE team15_projectdb").show()
spark.sql("SHOW TABLES").show()

print(spark.sql("SELECT * FROM team15_projectdb.car_vehicles_ext_part_bucket").show())


# Define the stages of the pipeline
stages = []
result_cols = numerical_cols

for cat_col in categorical_cols:
    cat_col_indexed = f"{cat_col}_index"
    cat_col_encoded = f"{cat_col}_encoded"

    string_indexer = StringIndexer(inputCol=cat_col, outputCol=cat_col_indexed)
    encoder = OneHotEncoder(inputCols=[cat_col_indexed], outputCols=[cat_col_encoded])

    stages += [string_indexer, encoder]
    result_cols += [cat_col_encoded]

# Location lat long to xyz
location_cols_in = ["latitude", "longitude"]
location_cols_out = ["x", "y", "z"]

latlong_transformer = LatLongToXYZ(
    inputCols=location_cols_in, outputCols=location_cols_out
)

stages += [latlong_transformer]
result_cols += location_cols_out

# Assemble the features
assembler = VectorAssembler(inputCols=result_cols, outputCol="features")
stages += [assembler]

# Create the pipeline
pipeline = Pipeline(stages=stages)


cars = spark.read.format("avro").table("team15_projectdb.car_vehicles_ext_part_bucket")

data = pipeline.fit(cars).transform(cars)
data = data.withColumnRenamed("price", "label")

(train_data, test_data) = data.randomSplit([0.8, 0.2])

# Create models
lr_model = LinearRegression(labelCol="label", featuresCol="features")
dt_model = DecisionTreeRegressor(labelCol="label", featuresCol="features")

# Create evaluators
evaluator = RegressionEvaluator(labelCol="label", predictionCol="prediction")

# Create hyperparameter optimization grid search
lr_grid_search = (
    ParamGridBuilder()
    .addGrid(lr_model.regParam, [0.0, 0.01, 0.1])
    .addGrid(lr_model.elasticNetParam, [0.5, 1.0])
    .build()
)

dt_grid_search = (
    ParamGridBuilder()
    .addGrid(dt_model.maxDepth, [3, 5, 7])
    .addGrid(dt_model.minInstancesPerNode, [1, 3, 5])
    .build()
)


def training_pipeline(model_name, model, evaluator, grid_search, train_data, test_data):
    cv = CrossValidator(
        estimator=model,
        estimatorParamMaps=grid_search,
        evaluator=evaluator,
        parallelism=5,
        numFolds=3,
    )

    # Search for best models
    cv_model = cv.fit(train_data)
    model_best = cv_model.bestModel

    # Save the best models
    model_best.write().overwrite().save(f"project/models/{model_name}")

    # Save the predictions
    predictions = model_best.transform(test_data)
    (
        predictions.select("label", "prediction")
        .coalesce(1)
        .write.mode("overwrite")
        .format("csv")
        .option("sep", ",")
        .option("header", "true")
        .save(f"project/output/{model_name}_predictions.csv")
    )

    return model_best, predictions


def get_model_metrics(evaluator, predictions):
    rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})
    r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})
    mae = evaluator.evaluate(predictions, {evaluator.metricName: "mae"})

    return rmse, r2, mae


# Run the training pipeline
lr_model_best, lr_preds = training_pipeline(
    "lr", lr_model, evaluator, lr_grid_search, train_data, test_data
)
dt_model_best, dt_preds = training_pipeline(
    "dt", dt_model, evaluator, dt_grid_search, train_data, test_data
)

# Create data frame to report performance of the models
models = [
    ["lr", *get_model_metrics(evaluator, lr_preds)],
    ["dt", *get_model_metrics(evaluator, dt_preds)],
]

df = spark.createDataFrame(models, ["model", "RMSE", "R2", "MAE"])
df.show(truncate=False)

# Save it to HDFS
(
    df.coalesce(1)
    .write.mode("overwrite")
    .format("csv")
    .option("sep", ",")
    .option("header", "true")
    .save("project/output/evaluation.csv")
)

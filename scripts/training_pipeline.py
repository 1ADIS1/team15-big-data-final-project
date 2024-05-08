from pyspark import keyword_only

from pyspark.ml import Pipeline, Transformer
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.param.shared import HasInputCols, HasOutputCols
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.regression import LinearRegression, DecisionTreeRegressor

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, FloatType


from wasabi import msg

import numpy as np


# Add here your team number teamx
TEAM = "team15"

# Location of your Hive database in HDFS
WAREHOUSE = "project/hive/warehouse"


CATEGORICAL_COLS = [
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

NUMERICAL_COLS = [
    "manufactured_year",
    "odometer",
]

LOCATION_COLS = ["latitude", "longitude"]


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


def get_pipeline() -> Pipeline:
    # Define the stages of the pipeline
    stages = []
    result_cols = NUMERICAL_COLS

    for cat_col in CATEGORICAL_COLS:
        cat_col_indexed = f"{cat_col}_index"
        cat_col_encoded = f"{cat_col}_encoded"

        string_indexer = StringIndexer(inputCol=cat_col, outputCol=cat_col_indexed)
        encoder = OneHotEncoder(
            inputCols=[cat_col_indexed], outputCols=[cat_col_encoded]
        )

        stages += [string_indexer, encoder]
        result_cols += [cat_col_encoded]

    # Location lat long to xyz
    location_cols_out = ["x", "y", "z"]

    latlong_transformer = LatLongToXYZ(
        inputCols=LOCATION_COLS, outputCols=location_cols_out
    )

    stages += [latlong_transformer]
    result_cols += location_cols_out

    # Assemble the features
    assembler = VectorAssembler(inputCols=result_cols, outputCol="features")
    stages += [assembler]

    # Create the pipeline
    pipeline = Pipeline(stages=stages)

    return pipeline


def get_model_metrics(evaluator: RegressionEvaluator, predictions):
    rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})
    r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})
    mae = evaluator.evaluate(predictions, {evaluator.metricName: "mae"})

    return rmse, r2, mae


def df_to(df, path, format="csv"):
    msg.info(f"Saving data to {path}...")
    (
        df.coalesce(1)
        .write.mode("overwrite")
        .format(format)
        .option("sep", ",")
        .option("header", "true")
        .save(path)
    )
    msg.good(f"Data saved to {path}")


def make_features_decriptions(spark):
    description = []

    for column in CATEGORICAL_COLS:
        description.append([column, "Transformed with OneHotEncoding"])

    for column in NUMERICAL_COLS:
        description.append([column, "No additional modifications"])

    for column in LOCATION_COLS:
        description.append([column, "Transformed to XYZ coordinate"])

    df_descriptions = spark.createDataFrame(
        description, ["feature_name", "feature_extraction_description"]
    )
    df_descriptions.show(truncate=False)

    df_to(df_descriptions, f"project/output/feature_extraction.csv")


def get_train_test_split(data, train_size: float = 0.8):
    train_data = data.limit(int(data.count() * 0.8))
    test_data = data.subtract(train_data)

    # Save the train and test data
    df_to(train_data, "project/output/train_data.json", format="json")
    df_to(test_data, "project/output/test_data.json", format="json")

    msg.good("Train and test data saved")

    return train_data, test_data


def main():
    spark = (
        SparkSession.builder.appName(f"{TEAM} - spark ML")
        .master("yarn")
        .config("hive.metastore.uris", "thrift://hadoop-02.uni.innopolis.ru:9883")
        .config("spark.executor.instances", 6)
        .config("spark.sql.warehouse.dir", WAREHOUSE)
        .config("spark.sql.avro.compression.codec", "snappy")
        .enableHiveSupport()
        .getOrCreate()
    )
    # spark.sparkContext.setLogLevel("WARN")
    msg.good("Spark session created")

    # We can also add
    # .config("spark.sql.catalogImplementation","hive")
    # But this is the default configuration
    # You can switch to Spark Catalog by setting "in-memory" for "spark.sql.catalogImplementation"
    msg.info("Testing connection to Hive")

    spark.sql("SHOW DATABASES").show()
    spark.sql("USE team15_projectdb")
    spark.sql("SHOW TABLES").show()

    spark.sql("SELECT * FROM team15_projectdb.car_vehicles_ext_part_bucket").show()

    # Get pipeline
    msg.info("Creating pipeline...")
    pipeline = get_pipeline()
    msg.good("Pipeline created")

    # Save feature extraction description
    msg.info("Extracting features...")
    make_features_decriptions(spark)
    msg.good("Feature extraction description saved")

    # Get data
    msg.info("Loading dataset...")
    cars = spark.read.format("avro").table(
        "team15_projectdb.car_vehicles_ext_part_bucket"
    )
    msg.good("Dataset loaded")

    data = pipeline.fit(cars).transform(cars)
    data = data.withColumnRenamed("price", "label")

    # Split data
    msg.info("Splitting dataset...")
    (train_data, test_data) = get_train_test_split(data, train_size=0.8)
    msg.good("Data splitted")

    outputs = {}

    # Train models
    for model_name in ["lr", "dt"]:
        evaluator = RegressionEvaluator(labelCol="label", predictionCol="prediction")

        if model_name == "lr":
            model = LinearRegression()
            msg.info("Training Linear Regression model")

            grid_search = (
                ParamGridBuilder()
                .addGrid(model.regParam, [0.01, 0.05, 0.1])
                .addGrid(model.elasticNetParam, [0.5, 1.0])
                .build()
            )
        elif model_name == "dt":
            model = DecisionTreeRegressor()
            msg.info("Training Decision Tree model")

            grid_search = (
                ParamGridBuilder()
                .addGrid(model.maxDepth, [5, 7, 10])
                .addGrid(model.minInstancesPerNode, [1, 3, 5])
                .build()
            )
        else:
            raise ValueError(f"Unknown model: {model_name}")

        cv = CrossValidator(
            estimator=model,
            estimatorParamMaps=grid_search,
            evaluator=evaluator,
            numFolds=3,
        )

        # Search for best models
        model_best = cv.fit(train_data).bestModel

        # Get and save the best models
        model_best.write().overwrite().save(f"project/models/{model_name}_model")
        msg.good(f"Model saved for {model_name}")

        # Get and save the predictions
        predictions = model_best.transform(test_data)

        df_to(
            predictions.select("label", "prediction"),
            f"project/output/{model_name}_predictions.csv",
        )
        msg.good(f"Predictions saved for {model_name}")

        # Get and save the best hyperparameters
        if model_name == "lr":
            hyperparams = {
                "regParam": model_best.getRegParam(),
                "elasticNetParam": model_best.getElasticNetParam(),
            }
        elif model_name == "dt":
            hyperparams = {
                "maxDepth": model_best.getMaxDepth(),
                "minInstancesPerNode": model_best.getMinInstancesPerNode(),
            }

        df_hyperparams = spark.createDataFrame([hyperparams], list(hyperparams.keys()))
        df_hyperparams.show(truncate=False)

        df_to(df_hyperparams, f"project/output/{model_name}_hyperparams.csv")
        msg.good(f"Hyperparameters saved for {model_name}")

        # Get and save the metrics
        metrics = get_model_metrics(evaluator, predictions)

        df_to(
            spark.createDataFrame([metrics], ["RMSE", "R2", "MAE"]),
            f"project/output/{model_name}_evaluation.csv",
        )
        msg.good(f"Metrics saved for {model_name}")

        # Save the model, predictions and metrics
        outputs[model_name] = (model_best, predictions, metrics)
        msg.good(f"Finished working on {model_name}")

    # Create data frame to report performance of the models
    df_models = spark.createDataFrame(
        [
            [str(outputs["lr"][0]), *outputs["lr"][2]],
            [str(outputs["dt"][0]), *outputs["dt"][2]],
        ],
        ["model", "RMSE", "R2", "MAE"],
    )
    msg.info("Model comparison")
    df_models.show(truncate=False)

    # Save model comparison
    df_to(df_models, "project/output/evaluation.csv")
    msg.good("Model comparison saved")

    spark.stop()
    msg.good("Spark session closed")
    msg.good("Done")


if __name__ == "__main__":
    main()

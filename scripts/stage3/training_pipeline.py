""" Training pipeline for the car price prediction project """

from typing import List, Tuple

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

LOCATION_COLS = [
    "latitude",
    "longitude",
]


class LatLongToXYZ(Transformer, HasInputCols, HasOutputCols):
    """Transform latitude and longitude to XYZ coordinates"""

    @keyword_only
    def __init__(
        self, inputCols: List[str] = None, outputCols: List[str] = None, **kwargs
    ):
        super().__init__()
        self._set(inputCols=inputCols, outputCols=outputCols, **kwargs)

    @staticmethod
    def to_xyz(
        lat: float, lon: float, alt: float = 0, in_radians: bool = False
    ) -> List[float]:
        """
        Convert latitude and longitude to XYZ coordinates

        :param lat: Latitude
        :param lon: Longitude
        :param alt: Altitude
        :param in_radians: If True, the input is in radians
        :return: XYZ coordinates
        """
        if not in_radians:
            lat = np.deg2rad(lat)
            lon = np.deg2rad(lon)
            alt = np.deg2rad(alt)

        semi_major_axis = 6378137  # WGS-84 semi-major axis
        e_squared = 6.6943799901377997e-3  # WGS-84 first eccentricity squared

        n_param = semi_major_axis / np.sqrt(1 - e_squared * np.sin(lat) * np.sin(lat))

        x_coord = (n_param + alt) * np.cos(lat) * np.cos(lon)
        y_coord = (n_param + alt) * np.cos(lat) * np.sin(lon)
        z_coord = (n_param * (1 - e_squared) + alt) * np.sin(lat)

        return [float(x_coord), float(y_coord), float(z_coord)]

    def _transform(self, dataset):
        """
        Transform the dataset

        :param dataset: Input dataset
        :return: Transformed dataset
        """
        # Define the UDF
        udf_type = ArrayType(FloatType())
        udf_func = udf(LatLongToXYZ.to_xyz, udf_type)

        # Get the input columns
        in_cols = dataset.select(self.getInputCols()).columns

        # Apply the UDF
        dataset = dataset.withColumn(self.getOutputCols()[0], udf_func(*in_cols)[0])
        dataset = dataset.withColumn(self.getOutputCols()[1], udf_func(*in_cols)[1])
        dataset = dataset.withColumn(self.getOutputCols()[2], udf_func(*in_cols)[2])

        return dataset


def get_pipeline() -> Pipeline:
    """Create the pipeline for the car price prediction project"""
    msg.info("Creating pipeline...")

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

    msg.good("Pipeline created")

    return pipeline


def get_model_metrics(
    evaluator: RegressionEvaluator, predictions
) -> Tuple[float, float, float]:
    """
    Get the model metrics for the predictions

    :param evaluator: The evaluator
    :param predictions: The predictions
    :return: The RMSE, R2 and MAE metrics
    """
    rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})
    r2_score = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})
    mae = evaluator.evaluate(predictions, {evaluator.metricName: "mae"})

    return rmse, r2_score, mae


def df_to(dataframe, path: str, out_format: str = "csv"):
    """
    Save the dataframe to the specified path

    :param dataframe: The dataframe to save
    :param path: The path to save the dataframe
    :param out_format: The format to save the dataframe
    """
    msg.info(f"Saving data to {path}...")
    (
        dataframe.coalesce(1)
        .write.mode("overwrite")
        .format(out_format)
        .option("sep", ",")
        .option("header", "true")
        .save(path)
    )
    msg.good(f"Data saved to {path}")


def make_features_descriptions(spark: SparkSession):
    """
    Create a dataframe with the feature extraction description

    :param spark: The Spark session
    """
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

    msg.info("Feature extraction description")
    df_descriptions.show(truncate=False)

    df_to(df_descriptions, "project/output/feature_extraction.csv")


def get_train_test_split(data, train_size: float = 0.8) -> Tuple:
    """
    Split the data into train and test sets

    :param data: The data to split
    :param train_size: The size of the train set
    :return: The train and test sets
    """
    train_data = data.limit(int(data.count() * train_size))
    test_data = data.subtract(train_data)

    # Save the train and test data
    df_to(train_data, "project/output/train_data.json", out_format="json")
    df_to(test_data, "project/output/test_data.json", out_format="json")

    msg.good("Train and test data saved")

    return train_data, test_data


def train_models(spark: SparkSession, train_data, test_data) -> dict:
    """
    Train the models and save the results

    :param spark: The Spark session
    :param train_data: The training data
    :param test_data: The test data
    :return: The trained models and their results
    """
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

        cross_val = CrossValidator(
            estimator=model,
            estimatorParamMaps=grid_search,
            evaluator=evaluator,
            numFolds=3,
        )

        # Search for best models
        model_best = cross_val.fit(train_data).bestModel

        # Get and save the best models
        msg.good(f"Best model for {model_name}")
        model_best.write().overwrite().save(f"project/models/{model_name}_model")

        # Get and save the predictions
        predictions = model_best.transform(test_data)

        df_to(
            predictions.select("label", "prediction"),
            f"project/output/{model_name}_predictions.csv",
        )

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

        msg.info(f"Hyperparameters for {model_name}")
        df_hyperparams.show(truncate=False)

        df_to(df_hyperparams, f"project/output/{model_name}_hyperparams.csv")

        # Get and save the metrics
        metrics = get_model_metrics(evaluator, predictions)

        df_to(
            spark.createDataFrame([metrics], ["RMSE", "R2", "MAE"]),
            f"project/output/{model_name}_evaluation.csv",
        )

        # Save the model, predictions and metrics
        outputs[model_name] = (model_best, predictions, metrics)
        msg.good(f"Finished working on {model_name}")

    return outputs


def main():
    """Training pipeline for the car price prediction project"""
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
    spark.sparkContext.setLogLevel("WARN")
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
    pipeline = get_pipeline()

    # Save feature extraction description
    make_features_descriptions(spark)

    # Get data
    cars = spark.read.format("avro").table(
        "team15_projectdb.car_vehicles_ext_part_bucket"
    )
    msg.good("Dataset loaded")

    data = pipeline.fit(cars).transform(cars).withColumnRenamed("price", "label")

    # Split data
    (train_data, test_data) = get_train_test_split(data, train_size=0.8)

    # Train models
    outputs = train_models(spark, train_data, test_data)

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

    spark.stop()
    msg.good("Spark session closed. Done")


if __name__ == "__main__":
    main()

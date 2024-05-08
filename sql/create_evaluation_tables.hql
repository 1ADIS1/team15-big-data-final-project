USE team15_projectdb;

-- Load LR model predictions
DROP TABLE IF EXISTS lr_predictions;
CREATE EXTERNAL TABLE lr_predictions(
label DOUBLE,
prediction DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/lr_predictions';

LOAD DATA INPATH 'project/output/lr_predictions.csv/*.csv' OVERWRITE INTO TABLE lr_predictions;

-- Load DT model predictions
DROP TABLE IF EXISTS dt_predictions;
CREATE EXTERNAL TABLE dt_predictions(
labrl DOUBLE,
prediction DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/dt_predictions';

LOAD DATA INPATH 'project/output/dt_predictions.csv/*.csv' OVERWRITE INTO TABLE dt_predictions;

-- load Comparison evaluations
DROP TABLE IF EXISTS evaluation;
CREATE EXTERNAL TABLE evaluation(
model STRING,
RMSE DOUBLE,
R2 DOUBLE,
MAE DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/evaluation';

LOAD DATA INPATH 'project/output/evaluation.csv/*.csv' OVERWRITE INTO TABLE evaluation;

-- load LR evaluations
DROP TABLE IF EXISTS lr_evaluation;
CREATE EXTERNAL TABLE lr_evaluation(
model STRING,
RMSE DOUBLE,
R2 DOUBLE,
MAE DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/lr_evaluation';

LOAD DATA INPATH 'project/output/lr_evaluation.csv/*.csv' OVERWRITE INTO TABLE lr_evaluation;

-- load LR evaluations
DROP TABLE IF EXISTS dt_evaluation;
CREATE EXTERNAL TABLE dt_evaluation(
model STRING,
RMSE DOUBLE,
R2 DOUBLE,
MAE DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/dt_evaluation';

LOAD DATA INPATH 'project/output/dt_evaluation.csv/*.csv' OVERWRITE INTO TABLE dt_evaluation;

-- load Hyper-parameters optimization for Linear Regression
DROP TABLE IF EXISTS lr_hyperparameters;
CREATE EXTERNAL TABLE lr_hyperparameters(
regParam DOUBLE,
elasticNetParam DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/lr_hyperparameters';

LOAD DATA INPATH 'project/output/lr_hyperparameters.csv/*.csv' OVERWRITE INTO TABLE lr_hyperparameters;

-- load Hyper-parameters optimization for Decision Tree
DROP TABLE IF EXISTS dt_hyperparameters;
CREATE EXTERNAL TABLE dt_hyperparameters(
maxDepth INT,
minInstancesPerNode INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/dt_hyperparameters';

LOAD DATA INPATH 'project/output/dt_hyperparameters.csv/*.csv' OVERWRITE INTO TABLE dt_hyperparameters;

-- load Feature extraction 
DROP TABLE IF EXISTS feature_extraction;
CREATE EXTERNAL TABLE feature_extraction(
feature_name STRING,
feature_extraction_description STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/feature_extraction';

LOAD DATA INPATH 'project/output/feature_extraction.csv/*.csv' OVERWRITE INTO TABLE feature_extraction;
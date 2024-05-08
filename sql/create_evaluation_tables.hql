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

-- Load DT model predictions
DROP TABLE IF EXISTS dt_predictions;
CREATE EXTERNAL TABLE dt_predictions(
labrl DOUBLE,
prediction DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/dt_predictions';

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

-- load Hyper-parameters optimization for Linear Regression
DROP TABLE IF EXISTS lr_hyperparams;
CREATE EXTERNAL TABLE lr_hyperparams(
regParam DOUBLE,
elasticNetParam DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/lr_hyperparams';

-- load Hyper-parameters optimization for Decision Tree
DROP TABLE IF EXISTS dt_hyperparams;
CREATE EXTERNAL TABLE dt_hyperparams(
maxDepth INT,
minInstancesPerNode INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/lr_hyperparams';

-- load Feature extraction 
DROP TABLE IF EXISTS feature_extraction;
CREATE EXTERNAL TABLE feature_extraction(
feature_name STRING,
feature_extraction_description STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/feature_extraction';

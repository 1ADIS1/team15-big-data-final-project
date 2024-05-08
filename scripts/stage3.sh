#!/bin/bash
source secrets/.psql.pass

# Clear models folder
# on HDFS
hdfs dfs -rm -r -f project/models

# and on local
rm -rf models
mkdir models

# Run training pipeline
spark-submit --master yarn scripts/training_pipeline.py

# Get models
hdfs dfs -get project/models/lr_model models/lr_model
hdfs dfs -get project/models/dt_model models/dt_model

hdfs dfs -cat project/output/lr_predictions.csv/*.csv > output/lr_predictions.csv
hdfs dfs -put -f output/lr_predictions.csv project/output/lr_predictions.csv/combined.csv
hdfs dfs -rm -r -f project/hive/warehouse/lr_prediction
hdfs dfs -mkdir project/hive/warehouse/lr_prediction
hdfs dfs -mv project/output/lr_predictions.csv/combined.csv project/hive/warehouse/lr_predictions


########################################################################################################################
hdfs dfs -cat project/output/lr_hyperparams.csv/*.csv > output/lr_predictions.csv
hdfs dfs -put -f output/lr_predictions.csv project/output/lr_hyperparams.csv/combined.csv
hdfs dfs -rm -r -f project/hive/warehouse/lr_hyperparams
hdfs dfs -mkdir project/hive/warehouse/lr_hyperparams
hdfs dfs -mv project/output/lr_hyperparams.csv/combined.csv project/hive/warehouse/lr_hyperparams
########################################################################################################################

# # Save combined version on HDFS

# hdfs dfs -cat project/output/feature_extraction.csv/*.csv > output/feature_extraction.csv
# hdfs dfs -put -f output/feature_extraction.csv project/output/feature_extraction.csv/combined.csv

# # Move predictions
# 
# hdfs dfs -cat project/output/dt_predictions.csv/*.csv > output/dt_predictions.csv

# # Save combined version on HDFS
# 
# hdfs dfs -put -f output/dt_predictions.csv project/output/dt_predictions.csv/combined.csv

# # Move predictions
# hdfs dfs -cat project/output/lr_hyperparams.csv/*.csv > output/lr_hyperparams.csv
# hdfs dfs -cat project/output/dt_hyperparams.csv/*.csv > output/dt_hyperparams.csv

# # Save combined version on HDFS
# hdfs dfs -put -f output/lr_hyperparams.csv project/output/lr_hyperparams.csv/combined.csv
# hdfs dfs -put -f output/dt_hyperparams.csv project/output/dt_hyperparams.csv/combined.csv

# # Move evaluations
# hdfs dfs -cat project/output/lr_evaluation.csv/*.csv > output/lr_evaluation.csv
# hdfs dfs -cat project/output/dt_evaluation.csv/*.csv > output/dt_evaluation.csv

# # Save combined version on HDFS
# hdfs dfs -put -f output/lr_evaluation.csv project/output/lr_evaluation.csv/combined.csv
# hdfs dfs -put -f output/dt_evaluation.csv project/output/dt_evaluation.csv/combined.csv

# # Move comparison
# hdfs dfs -cat project/output/evaluation.csv/*.csv > output/evaluation.csv

# # Save combined version on HDFS
# hdfs dfs -put -f output/evaluation.csv project/output/evaluation.csv/combined.csv

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_evaluation_tables.hql

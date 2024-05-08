#!/bin/bash
source secrets/.psql.pass

spark-submit --master yarn scripts/training_pipeline.py

# Clear models folder
# on HDFS
hdfs dfs -rm -r -f project/models

# and on local
rm -rf models
mkdir models

# Get models
hdfs dfs -get project/models/lr_model models/lr_model
hdfs dfs -get project/models/dt_model models/dt_model

# Move predictions
hdfs dfs -cat project/output/lr_predictions.csv/*.csv > output/lr_predictions.csv
hdfs dfs -cat project/output/dt_predictions.csv/*.csv > output/dt_predictions.csv

# Move predictions
hdfs dfs -cat project/output/lr_hyperparams.csv/*.csv > output/lr_hyperparams.csv
hdfs dfs -cat project/output/dt_hyperparams.csv/*.csv > output/dt_hyperparams.csv

# Move evaluations
hdfs dfs -cat project/output/lr_evaluation.csv/*.csv > output/lr_evaluation.csv
hdfs dfs -cat project/output/dt_evaluation.csv/*.csv > output/dt_evaluation.csv

# Move comparison
hdfs dfs -cat project/output/evaluation.csv/*.csv > output/evaluation.csv

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_evaluation_tables.hql

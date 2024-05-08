#!/bin/bash
source secrets/.psql.pass

python3 scripts/training_pipeline.py

# Put models on HDFS
hdfs dfs -get models/lr_model models/lr_model
hdfs dfs -get models/dt_model models/dt_model

# Put predictions
hdfs dfs -cat output/lr_predictions.csv/*.csv > project/output/lr_predictions.csv
hdfs dfs -cat output/dt_predictions.csv/*.csv > project/output/dt_predictions.csv

# Put hyperparameters
hdfs dfs -cat output/lr_hyperparams.csv/*.csv > project/output/lr_hyperparams.csv
hdfs dfs -cat output/dt_hyperparams.csv/*.csv > project/output/dt_hyperparams.csv

# Put evaluations
hdfs dfs -cat output/lr_evaluation.csv/*.csv > project/output/lr_evaluation.csv
hdfs dfs -cat output/dt_evaluation.csv/*.csv > project/output/dt_evaluation.csv

# Put comparison
hdfs dfs -cat output/evaluation.csv/*.csv > project/output/evaluation.csv

hdfs dfs -put -f output/lr_predictions.csv project/output
hdfs dfs -put -f output/dt_predictions.csv project/output
hdfs dfs -put -f output/evaluation.csv project/output
hdfs dfs -put -f output/lr_evaluation.csv project/output
hdfs dfs -put -f output/dt_evaluation.csv project/output
hdfs dfs -put -f output/lr_hyperparameters.csv project/output
hdfs dfs -put -f output/dt_hyperparameters.csv project/output
hdfs dfs -put -f output/feature_extraction.csv project/output

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_evaluation_tables.hql

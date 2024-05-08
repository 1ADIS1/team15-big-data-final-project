#!/bin/bash
source secrets/.psql.pass

hdfs dfs -put -f output/lr_predictions.csv project/output
hdfs dfs -put -f output/dt_predictions.csv project/output
hdfs dfs -put -f output/evaluation.csv project/output
hdfs dfs -put -f output/lr_evaluation.csv project/output
hdfs dfs -put -f output/dt_evaluation.csv project/output
hdfs dfs -put -f output/lr_hyperparameters.csv project/output
hdfs dfs -put -f output/dt_hyperparameters.csv project/output
hdfs dfs -put -f output/feature_extraction.csv project/output

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_evaluation_tables.hql

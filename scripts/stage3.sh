#!/bin/bash
source secrets/.psql.pass

# Clear models folder
# ...on HDFS
hdfs dfs -rm -r -f project/models

# ...and on local
rm -rf models
mkdir models

# Run training pipeline
spark-submit --master yarn scripts/training_pipeline.py

# Define function to merge CSVs and transfer them to HDFS and Hive
function merge_csv_and_transfer() {
  if [ -z "$1" ]
  then
    echo "No argument supplied"
    return
  fi

  path_hdfs="project/output/$1.csv/"
  path_local="output/$1.csv"
  path_hive="project/hive/warehouse/$1"

  hdfs dfs -cat $path_hdfs/*.csv > $path_local # Merge CSVs to local
  hdfs dfs -put -f $path_local $path_hdfs/combined.csv # Transfer to HDFS
  hdfs dfs -rm -r -f $path_hive # Remove old data
  hdfs dfs -mkdir $path_hive # Create directory
  hdfs dfs -mv $path_hdfs/combined.csv $path_hive # Move combined CSV to Hive
}

# Get models
hdfs dfs -get project/models/lr_model models/lr_model
hdfs dfs -get project/models/dt_model models/dt_model

# Get predictions
merge_csv_and_transfer lr_predictions
merge_csv_and_transfer dt_predictions

# Get hyperparameters
merge_csv_and_transfer lr_hyperparams
merge_csv_and_transfer dt_hyperparams

# Get evaluations
merge_csv_and_transfer lr_evaluation
merge_csv_and_transfer dt_evaluation

# Get comparison
merge_csv_and_transfer evaluation

# Get feature extraction
merge_csv_and_transfer feature_extraction


beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_evaluation_tables.hql

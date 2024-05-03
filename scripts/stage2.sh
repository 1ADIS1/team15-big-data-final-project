#!/bin/bash
source secrets/.psql.pass

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_partitioned_tables.hql

# 1st query
# Clean outputs
hdfs dfs -rm -r project/output/q1
hdfs dfs -rm -r project/hive/warehouse/q1

echo "US_state,total_vehicles" > output/q1.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q1.hql
hdfs dfs -cat project/output/q1/* >> output/q1.csv

# 2nd query
# Clean outputs
hdfs dfs -rm -r project/output/q2
hdfs dfs -rm -r project/hive/warehouse/q2

echo "US_state,avg_price" > output/q2.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q2.hql
hdfs dfs -cat project/output/q1/* >> output/q2.csv

# 3rd query
# Clean outputs
hdfs dfs -rm -r project/output/q3
hdfs dfs -rm -r project/hive/warehouse/q3

echo "US_state,avg_mileage" > output/q3.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q3.hql
hdfs dfs -cat project/output/q1/* >> output/q3.csv

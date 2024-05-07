#!/bin/bash
source secrets/.psql.pass

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_partitioned_tables.hql

# 1st query
# Clean outputs
hdfs dfs -rm -r project/output/q1
hdfs dfs -rm -r project/hive/warehouse/q1
# Run script and write inputs
echo "US_state,total_vehicles" > output/q1.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q1.hql
hdfs dfs -cat project/output/q1/* >> output/q1.csv

# 2nd query
# Clean outputs
hdfs dfs -rm -r project/output/q2
hdfs dfs -rm -r project/hive/warehouse/q2
# Run script and write inputs
echo "US_state,avg_price" > output/q2.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q2.hql
hdfs dfs -cat project/output/q2/* >> output/q2.csv

# 3rd query
# Clean outputs
hdfs dfs -rm -r project/output/q3
hdfs dfs -rm -r project/hive/warehouse/q3
# Run script and write inputs
echo "US_state,median_mileage" > output/q3.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q3.hql
hdfs dfs -cat project/output/q3/* >> output/q3.csv

# 4th query
# Clean outputs
hdfs dfs -rm -r project/output/q4
hdfs dfs -rm -r project/hive/warehouse/q4
# Run script and write inputs
echo "US_state,count_cars" > output/q4.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q4.hql
hdfs dfs -cat project/output/q4/* >> output/q4.csv

# 5th query
# Clean outputs
hdfs dfs -rm -r project/output/q5
hdfs dfs -rm -r project/hive/warehouse/q5
# Run script and write inputs
echo "US_state,count_years" > output/q5.csv 
beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q5.hql
hdfs dfs -cat project/output/q5/* >> output/q5.csv

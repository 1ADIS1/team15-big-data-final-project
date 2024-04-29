#!/bin/bash
source secrets/.psql.pass

hdfs dfs -mkdir -p project/output/q1

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_partitioned_tables.hql

# beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q1.hql --hiveconf hive.resultset.use.unique.column.names=false > output/q1.csv

# beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q2.hql --hiveconf hive.resultset.use.unique.column.names=false > output/q2.csv

# beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q3.hql --hiveconf hive.resultset.use.unique.column.names=false > output/q3.csv


# Add a header to the output file
echo "US_state,total_vehicles" > output/q1.csv 

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/q1.hql

# concatenate all file partitions and 
# append the output to the file output/q1.csv
hdfs dfs -cat project/output/q1/* >> output/q1.csv

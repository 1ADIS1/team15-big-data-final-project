#!/bin/bash
source secrets/.psql.pass

# Import to PSQL
python3 scripts/build_projectdb.py

# Clear HDFS warehouse folder before transfer
hdfs dfs -rm -r project/warehouse
hdfs dfs -mkdir project/warehouse

# Transfer data from PSQL to HDFS
sqoop import-all-tables --connect jdbc:postgresql://hadoop-04.uni.innopolis.ru/team15_projectdb --username team15 --password $password --compression-codec=snappy --compress --as-avrodatafile --warehouse-dir=project/warehouse --m 1

# Move generated files to output folder
mv *.avsc output
mv *.java output

# Now move files from output to hdfs/warehouse
hdfs dfs -mkdir -p project/warehouse/avsc
hdfs dfs -put -f output/*.avsc project/warehouse/avsc

# Import to PSQL
python scripts/build_projectdb.py

# TODO: add password secret
password=pytttPLjPeOI7kc1

# Transfer data from PSQL to HDFS
sqoop import-all-tables --connect jdbc:postgresql://hadoop-04.uni.innopolis.ru/team15_projectdb --username team15 --password $password --compression-codec=snappy --compress --as-avrodatafile --warehouse-dir=project/warehouse --m 1

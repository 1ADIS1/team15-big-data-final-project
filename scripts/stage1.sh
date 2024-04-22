# Import to PSQL
python scripts/build_projectdb.py

# TODO: add password secret
password=pytttPLjPeOI7kc1

# Clear HDFS warehouse folder before transfer
sqoop import --connect jdbc:postgresql://hadoop-04.uni.innopolis.ru/team15_projectdb --username team15 --password $password --table car_description --delete-target-dir --target-dir 'project/warehouse/' -m 1

# Transfer data from PSQL to HDFS
sqoop import-all-tables --connect jdbc:postgresql://hadoop-04.uni.innopolis.ru/team15_projectdb --username team15 --password $password --compression-codec=snappy --compress --as-avrodatafile --warehouse-dir=project/warehouse --m 1

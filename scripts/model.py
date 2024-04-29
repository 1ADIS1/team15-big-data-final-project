from pyspark.sql import SparkSession

# Add here your team number teamx
team = "team15"


# location of your Hive database in HDFS
warehouse = "project/hive/warehouse"

spark = SparkSession.builder\
        .appName("{} - spark ML".format(team))\
        .master("yarn")\
        .config("hive.metastore.uris", "thrift://hadoop-02.uni.innopolis.ru:9883")\
        .config("spark.sql.warehouse.dir", warehouse)\
        .config("spark.sql.avro.compression.codec", "snappy")\
        .enableHiveSupport()\
        .getOrCreate()

#We can also add
# .config("spark.sql.catalogImplementation","hive")\ 
# But this is the default configuration
# You can switch to Spark Catalog by setting "in-memory" for "spark.sql.catalogImplementation"


spark.sql("SHOW DATABASES").show()
spark.sql("USE team15_projectdb").show()
spark.sql("SHOW TABLES").show()
print(spark.sql("SELECT * FROM team15_projectdb.car_vehicles_ext_part_bucket").show())

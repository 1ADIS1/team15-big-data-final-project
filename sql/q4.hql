USE team15_projectdb;

DROP TABLE IF EXISTS q4_results;
CREATE EXTERNAL TABLE q4_results(
manufacturer STRING,
count_cars INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q4'; 

SET hive.resultset.use.unique.column.names = false;

-- q4
INSERT INTO q4_results
SELECT 
DISTINCT
manufacturer,
COUNT(*) OVER(PARTITION BY manufacturer) as count_cars
FROM car_vehicles_ext_part_bucket;

INSERT OVERWRITE DIRECTORY 'project/output/q4' 
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
SELECT manufacturer, count_cars FROM q4_results
ORDER BY count_cars DESC;

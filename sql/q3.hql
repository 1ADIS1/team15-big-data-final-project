USE team15_projectdb;

DROP TABLE IF EXISTS q3_results;
CREATE EXTERNAL TABLE q3_results(
US_state STRING,
median_mileage DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q3'; 

SET hive.resultset.use.unique.column.names = false;

-- q3
INSERT INTO q3_results
SELECT 
DISTINCT
CONCAT('US-', UPPER(US_state)),
PERCENTILE(odometer, 0.5) OVER (PARTITION BY US_state) as median_mileage
FROM car_vehicles_ext_part_bucket;

INSERT OVERWRITE DIRECTORY 'project/output/q3' 
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
SELECT US_state, median_mileage FROM q3_results
ORDER BY median_mileage DESC;

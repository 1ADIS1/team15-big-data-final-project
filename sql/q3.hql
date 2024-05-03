USE team15_projectdb;

DROP TABLE IF EXISTS q3_results;
CREATE EXTERNAL TABLE q3_results(
US_state STRING,
avg_mileage DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q3'; 

SET hive.resultset.use.unique.column.names = false;

-- q3
INSERT INTO q3_results
SELECT 
US_state,
AVG(mileage) as avg_mileage
FROM car_vehicles_ext_part_bucket
GROUP BY US_state
ORDER BY avg_mileage DESC;

INSERT OVERWRITE DIRECTORY 'project/output/q3' 
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
SELECT US_state, avg_mileage FROM q3_results
ORDER BY avg_mileage DESC
LIMIT 15;




USE team15_projectdb;

DROP TABLE IF EXISTS q2_results;
CREATE EXTERNAL TABLE q2_results(
US_state STRING,
avg_price DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q2'; 

SET hive.resultset.use.unique.column.names = false;

-- q2
INSERT INTO q2_results
SELECT 
US_state,
AVG(price) OVER (PARTITION BY US_state) as avg_price
FROM car_vehicles_ext_part_bucket;

INSERT OVERWRITE DIRECTORY 'project/output/q2' 
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
SELECT US_state, avg_price FROM q2_results
ORDER BY avg_price DESC
LIMIT 15;

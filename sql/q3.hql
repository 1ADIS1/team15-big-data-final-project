USE team15_projectdb;

DROP TABLE IF EXISTS q3_results;
CREATE EXTERNAL TABLE q3_results(
US_state STRING,
states_avg_mileage DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q3'; 

SET hive.resultset.use.unique.column.names = false;

-- q3
INSERT INTO q3_results
SELECT 
US_state,
AVG(mileage) OVER (PARTITION BY US_state) as states_avg_mileage
FROM car_vehicles_ext_part_bucket
ORDER BY states_avg_price ASC
LIMIT 15;

SELECT * FROM q3_results;

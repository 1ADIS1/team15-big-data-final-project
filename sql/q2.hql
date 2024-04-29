USE team15_projectdb;

DROP TABLE IF EXISTS q2_results;
CREATE EXTERNAL TABLE q2_results(
US_state STRING,
total_vehicles INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q2'; 

SET hive.resultset.use.unique.column.names = false;

-- q1
INSERT INTO q2_results
SELECT 
AVG(price) OVER (PARTITION BY US_state) as states_avg_price
FROM car_vehicles_ext_part_bucket
ORDER BY states_avg_price ASC
LIMIT 15;

SELECT * FROM q2_results;

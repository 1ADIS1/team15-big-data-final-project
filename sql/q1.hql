USE team15_projectdb;

DROP TABLE IF EXISTS q1_results;
CREATE EXTERNAL TABLE q1_results(
US_state STRING,
total_vehicles INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q1'; 

SET hive.resultset.use.unique.column.names = false;

-- q1
INSERT INTO q1_results
SELECT 
US_state,
COUNT(entry_ID) as total_vehicles
FROM car_vehicles_ext_part_bucket
GROUP BY US_state
ORDER BY total_vehicles ASC
LIMIT 15;

SELECT * FROM q1_results;
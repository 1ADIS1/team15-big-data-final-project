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
ORDER BY total_vehicles DESC;

INSERT OVERWRITE DIRECTORY 'project/output/q1' 
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
SELECT US_state, total_vehicles FROM q1_results
ORDER BY total_vehicles DESC
LIMIT 15;

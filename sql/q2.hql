USE team15_projectdb;

-- create table q2_results
DROP TABLE IF EXISTS q1_results;
CREATE EXTERNAL TABLE q1_results(
    US_state STRING,
    total_vehicles INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q2';

SET hive.resultset.use.unique.column.names = false;

-- q2
--SELECT 

SELECT * FROM q1_results;

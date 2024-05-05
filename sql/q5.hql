USE team15_projectdb;

DROP TABLE IF EXISTS q5_results;
CREATE EXTERNAL TABLE q5_results(
manufactured_year INT,
count_years INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q5'; 

SET hive.resultset.use.unique.column.names = false;

-- q4
INSERT INTO q5_results
SELECT 
DISTINCT
manufactured_year,
COUNT(*) OVER(PARTITION BY manufactured_year) as count_years
FROM car_vehicles_ext_part_bucket;

INSERT OVERWRITE DIRECTORY 'project/output/q5' 
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
SELECT manufactured_year, count_years FROM q5_results
ORDER BY count_years DESC;

DROP DATABASE IF EXISTS team15_projectdb CASCADE;

-- Create db
CREATE DATABASE team15_projectdb LOCATION "project/hive/warehouse";
USE team15_projectdb;

DROP TABLE IF EXISTS car_description;

-- Create and load tables to hive
CREATE EXTERNAL TABLE car_description STORED AS AVRO LOCATION
'project/warehouse/car_description' TBLPROPERTIES
('avro.schema.url'='project/warehouse/avsc/car_description.avsc');

-- Check tables
SELECT * FROM car_description
LIMIT 100;

DROP DATABASE IF EXISTS team15_projectdb CASCADE;

-- Create db
CREATE DATABASE team15_projectdb LOCATION "project/hive/warehouse";
USE team15_projectdb;

DROP TABLE IF EXISTS car_description;

-- Create and load tables to hive
CREATE EXTERNAL TABLE car_description STORED AS AVRO LOCATION
'project/warehouse/output' TBLPROPERTIES
('avro.schema.url'='project/warehouse/avsc/vehicles.avsc');

-- Check tables
SELECT COUNT(1) FROM car_description;
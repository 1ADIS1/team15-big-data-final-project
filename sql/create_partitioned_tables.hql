USE team15_projectdb;

SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.exec.dynamic.partition = true;
SET hive.enforce.bucketing = true;

DROP TABLE IF EXISTS car_vehicles_ext_part_bucket;

CREATE EXTERNAL TABLE car_vehicles_ext_part_bucket (
    entry_ID BIGINT,
    region_url VARCHAR(255),
    price BIGINT,
    manufactured_year INT,
    manufacturer VARCHAR(255),
    car_condition VARCHAR(255),
    cylinders VARCHAR(255),
    fuel VARCHAR(255),
    odometer INT,
    transmission VARCHAR(255),
    car_drive VARCHAR(255),
    car_size VARCHAR(255),
    car_type VARCHAR(255),
    paint_color VARCHAR(255),
    latitude DOUBLE,
    longitude DOUBLE
)
PARTITIONED BY (
    US_state VARCHAR(255)
)
CLUSTERED BY (entry_ID) INTO 3 buckets
STORED AS AVRO LOCATION
'project/hive/warehouse/car_vehicles_ext_part_bucket'
TBLPROPERTIES ('AVRO.COMPRESS' = 'SNAPPY');

INSERT INTO car_vehicles_ext_part_bucket
PARTITION (
    US_state
)
SELECT 
    entry_ID,
    region_url,
    price,
    manufactured_year,
    manufacturer,
    car_condition,
    cylinders,
    fuel,
    odometer,
    transmission,
    car_drive,
    car_size,
    car_type,
    paint_color,
    latitude,
    longitude,
    US_state
FROM car_description;

DROP TABLE IF EXISTS car_description;

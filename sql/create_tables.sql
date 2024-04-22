START TRANSACTION;

DROP TABLE IF EXISTS car_description;

CREATE TABLE IF NOT EXISTS car_description (
	entry_ID BIGINT NOT NULL PRIMARY KEY,
	region_url VARCHAR(255),
	price BIGINT NOT NULL,
	manufactured_year INTEGER,
	manufacturer VARCHAR(255),
	model VARCHAR(255),
	car_condition VARCHAR(255),
	cylinders VARCHAR(255),
	fuel VARCHAR(255),
	odometer INTEGER,
	transmission VARCHAR(255),
	car_drive VARCHAR(255),
	car_size VARCHAR(255),
	car_type VARCHAR(255),
	paint_color VARCHAR(255),
	US_state VARCHAR(255),
	latitude REAL NOT NULL,
	longitude REAL NOT NULL
);

ALTER DATABASE team15_projectdb SET datestyle TO iso, ymd;

COMMIT;
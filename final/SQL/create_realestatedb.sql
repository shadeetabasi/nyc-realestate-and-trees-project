-- creating table schema to load real estate data from CSV
CREATE TABLE real_estate_data_final (
id Serial PRIMARY KEY,
full_address VARCHAR(255),
building_class_category VARCHAR(255),
sale_price FLOAT,
neighborhood VARCHAR(255),
tax_class_at_present VARCHAR(255),
zip_code INT,
building_class_at_time_of_sale VARCHAR(255),
borough_name VARCHAR(255),
latitude FLOAT,
longitude FLOAT
);
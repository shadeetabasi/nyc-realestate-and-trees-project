-- creating tablse schema to load data from CSV
CREATE TABLE real_estate_data (
id Serial PRIMARY KEY,
full_address VARCHAR,
sale_price FLOAT,
neighborhood VARCHAR,
tax_class_at_present VARCHAR,
zip_code FLOAT,
building_class_at_time_of_sale VARCHAR,
borough_name VARCHAR,
latitude FLOAT,
longitude FLOAT
);


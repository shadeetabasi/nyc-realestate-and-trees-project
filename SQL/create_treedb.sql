CREATE TABLE new_york_tree_census_data (
id Serial PRIMARY KEY,
tree_id INT,
stump_diam INT,
status VARCHAR(255),
health VARCHAR(255),
spc_latin VARCHAR(255),
spc_common VARCHAR(255),
tree_address VARCHAR(255),
zipcode INT,
boroname VARCHAR(255),
nta_name VARCHAR(255),
latitude FLOAT,
longitude FLOAT
);
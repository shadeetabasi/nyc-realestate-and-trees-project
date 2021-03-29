#!/usr/bin/env python
# coding: utf-8

#Setup and import dependencies
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import pandas as pd

## Please note this is using Shadee's postgres password which is also postgres
connection_string = "postgres:postgres@localhost:5432/group_project_2"

print("Reading data")
new_york_tree_census_2015_dataset = "new_york_tree_census_2015.csv"
new_york_tree_census_2015_df = pd.read_csv(new_york_tree_census_2015_dataset)



new_new_york_tree_census_2015_df = new_york_tree_census_2015_df[['tree_id', 'stump_diam', 'status', 'health', 'spc_latin', 'spc_common', 'address', 'zipcode', 'boroname', 'nta_name', 'latitude', 'longitude']].copy()

new_new_york_tree_census_2015_df['spc_latin_for_join']=new_new_york_tree_census_2015_df['spc_latin'].str.strip().copy()
new_new_york_tree_census_2015_df['spc_latin_for_join']=new_new_york_tree_census_2015_df['spc_latin_for_join'].str.replace(" ",'').copy()
new_new_york_tree_census_2015_df['spc_latin_for_join']=new_new_york_tree_census_2015_df['spc_latin_for_join'].str.lower().copy()

print("Cleaning data, dropping duplicates")
chars = "\`*_{}[]()>#+-.,!$:;%'&/?"
for c in chars:
    new_new_york_tree_census_2015_df['spc_latin_for_join'] = new_new_york_tree_census_2015_df['spc_latin_for_join'].str.replace(c,"")

clean_new_york_tree_census_2015_df = new_new_york_tree_census_2015_df.drop_duplicates()




# clean_new_york_tree_census_2015_df.to_csv(r'../dramane/clean_new_york_tree_census_2015_data.csv', index = False)


# # Create Engine to Database Connection
print("connecting to DB")
engine = create_engine(f'postgresql://{connection_string}')

# Confirm tables
print("table names:")
print(engine.table_names())

# # Load DataFrames into Database


#Reset index name to load into SQL database
clean_new_york_tree_census_2015_df.index.name = "id"


updated_tree_census_data = clean_new_york_tree_census_2015_df.rename(columns={"address": "tree_address"})

print("Uploading to new table")
updated_tree_census_data.to_sql(name='new_york_tree_census_data_final', con=engine, if_exists='fail', index=True)


print("IT RAN!")


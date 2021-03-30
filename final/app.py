# Now that you have completed your initial analysis, design a Flask API 
# based on the queries that you have just developed.

# Set up Dependencies 
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template, redirect
import json
from pprint import pprint
from random import sample

# Flask Setup
app = Flask(__name__)
app.static_folder = 'static'

#Create connection to sql database - does this need to change so we delete the blank table?
connection_string = "postgres:postgres@localhost:5432/group_project_2"
engine = create_engine(f'postgresql://{connection_string}')


#################################################
# Flask Routes
#################################################

# /
# Home page
# List all routes that are available
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/leafletmap")
def leafletmap():
    # 
    map_data = []
    query = """SELECT latitude, longitude, spc_common, boroname, health 
                FROM public.new_york_tree_census_data_final"""
    # Open a connection to SQL
    connection = engine.connect()
    # Execute query
    result = engine.execute(query)
    # Append each result to our list
    for row in result:
        map_data.append(row)
    # Close the connection
    connection.close()

    # Take random sample for development purposes
    map_data = sample(map_data, 100)

    # Return template and data
    # Note: follow this example for how to pass into a map
    # https://stackoverflow.com/questions/42499535/passing-a-json-object-from-flask-to-javascript
    return render_template("leafletmap.html", map_data=map_data)

@app.route("/realestatedashboard")
def realestatedashboard():
     # 
    all_data = []
    query = """SELECT latitude, longitude, borough_name, sale_price, building_class_category
                FROM public.real_estate_data"""
    # Open a connection to SQL
    connection = engine.connect()
    # Execute query
    result = engine.execute(query)
    # Append each result to our list
    for row in result:
        all_data.append(row)
    # Close the connection
    connection.close()

    # Convert to a DF, group by boro and species
    df = pd.DataFrame(all_data, columns = ["latitude", "longitude", "borough_name", "sale_price", "building_class_category"])
    grouped = df.groupby(["borough_name", "building_class_category"]).agg({"sale_price":"count"})

    # Format data for D3
    bar_data = {}
    for borough in df.borough_name.unique():
        subdf = grouped.loc[borough]
        top15 = subdf.sort_values(by='sale_price', ascending=False).iloc[:15]
        y = list(top15.index)
        x = list(top15.sale_price)
        bar_data[borough] = {"x": x, "y": y}
    # Return template and data
    return render_template("realestatedashboard.html", bar_data= bar_data, boroughs = list(bar_data.keys()))

@app.route("/treedashboard")
def treedashboard():
    # 
    all_data = []
    query = """SELECT latitude, longitude, spc_common, boroname, health 
                FROM public.new_york_tree_census_data_final"""
    # Open a connection to SQL
    connection = engine.connect()
    # Execute query
    result = engine.execute(query)
    # Append each result to our list
    for row in result:
        all_data.append(row)
    # Close the connection
    connection.close()

    # Convert to a DF, group by boro and species
    df = pd.DataFrame(all_data, columns = ["latitude", "longitude", "spc_common", "boroname", "health"])
    grouped = df.groupby(["boroname", "spc_common"]).agg({"health":"count"})

    # Format data for D3
    bar_data = {}
    for boro in df.boroname.unique():
        subdf = grouped.loc[boro]
        top15 = subdf.sort_values(by='health', ascending=False).iloc[:15]
        y = list(top15.index)
        x = list(top15.health)
        bar_data[boro] = {"x": x, "y": y}
    # Return template and data
    return render_template("treedashboard.html", bar_data= bar_data, boros = list(bar_data.keys()))


@app.route("/scrape")
def scrape():

    # Redirect back to home page
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
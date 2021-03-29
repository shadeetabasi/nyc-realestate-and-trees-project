# Now that you have completed your initial analysis, design a Flask API 
# based on the queries that you have just developed.

# Set up Dependencies 
import numpy as np
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

# reflect an existing database into a new model - still needed?
Base = automap_base() 

# reflect the tables - IS THIS STILL NEEDED?
Base.prepare(engine, reflect=True) 

# Save references to each table - IS THIS STILL NEEDED?
# measurement = Base.classes.measurement
# station = Base.classes.station

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

    return render_template("realestatedashboard.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/treedashboard")
def treedashboard():
    return render_template("treedashboard.html")

@app.route("/treedata")
def treedata():
    return render_template("treedata.html")

@app.route("/scrape")
def scrape():

    # Redirect back to home page
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
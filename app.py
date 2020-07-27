# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
# app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)

# -- Routes section --

# HOMEPAGE

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
    

# INDEX

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello World"

# def index():
#     return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA


# @app.route('/add')

# def add():
    # connect to the database

    # insert new data

    # return a message to the use

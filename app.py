# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
# from model import getImageUrlFrom
from flask_pymongo import PyMongo
import os
import requests


# sudo pip3 install dnspython

# -- Initialization section --
app = Flask(__name__)

# <<<<<<< HEAD
app.config['GIPHY_KEY'] = os.getenv("GIPHY_KEY")

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]

# >>>>>>> 157c480e2b8dca608729a51a01ec0a15e8c8e88d
# name of database
app.config['MONGO_DBNAME'] = 'cook'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://recipe_reader:ccwAiFDz5VKmV5dA@cluster0.nayre.mongodb.net/cook?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --

# HOMEPAGE

@app.route('/')
# <<<<<<< HEAD
# @app.route('/index')
# def index():
#     return render_template("index.html", time = datetime.now())
# =======
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
# >>>>>>> 157c480e2b8dca608729a51a01ec0a15e8c8e88d


# CONNECT TO DB, ADD DATA


# <<<<<<< HEAD
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

 
# ________________________________________Routes section API/Learn More________________________________________________________

# app.config['GIPHY_KEY'] = 'https://tripadvisor1.p.rapidapi.com/restaurants/list'
response = requests.get('https://tripadvisor1.p.rapidapi.com/restaurants/list').json()
querystring = {"restaurant_tagcategory_standalone":"10591","lunit":"km","restaurant_tagcategory":"10591","limit":"30","restaurant_mealtype":"lobster","currency":"USD","lang":"en_US","location_id":"293919"}

headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "a5f304028dmsh7d1413cbfff8d76p13efabjsnf5bba74c75e5"
    }


@app.route('/learn_more')
def learn_more():
    return render_template('learn_more.html')

@app.route('/restaurant', methods = ['POST', 'GET'])

def restaurant():
    if request.method == 'POST':
        mychoice = request.form['restaurantchoice']
        source = requests.get(mychoice, response, headers=headers, params=querystring)
        return render_template("restaurant.html", time = datetime.now(), source=source)
    else:
        return "error"


# ________________________________________End Section of API_______________________________________________________ 
@app.route('/type_of_recipe')
def type_of_recipe():
    return render_template('type_of_recipe.html')


#_________________________________________Community Page__________________________________________________________
@app.route('/community')
def community():
    recipe_collection = mongo.db.recipe
    recipe = recipe_collection.find({})
    return render_template("community.html", recipe=recipe, time = datetime.now())
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        user_name = request.form['user_name']
        user_recipe = request.form['user_recipe']
        user_comment = request.form['user_comment']
      
        recipe_collection = mongo.db.recipe
        recipe_collection.insert_one({'user': user_name, 'recipe': user_recipe, 'comment': user_comment})
        recipe = recipe_collection.find({})
        return render_template("community.html", recipe=recipe, time = datetime.now())

# _______________________________________End Community Page______________________________________________________

# @app.route('/add')

# @app.route('/add')

# >>>>>>> 157c480e2b8dca608729a51a01ec0a15e8c8e88d
# def add():
    # connect to the database

    # insert new data

# <<<<<<< HEAD
    # return a message to the user
    # return ""

# ------------Below is the new information waiting to be add------------------------------------------
# =======
    # return a message to the use
# >>>>>>> 157c480e2b8dca608729a51a01ec0a15e8c8e88d

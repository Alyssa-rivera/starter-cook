# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from model import getRecipe
from model import fix_query
# from model import getImageUrlFrom
from flask_pymongo import PyMongo
import os


# sudo pip3 install dnspython

# -- Initialization section --
app = Flask(__name__)

# app.config['GIPHY_KEY'] = os.getenv("GIPHY_KEY")
app.config['TRIP_KEY'] = 'a5f304028dmsh7d1413cbfff8d76p13efabjsnf5bba74c75e5'
# .env will not be push to git hub 



# name of database
app.config['MONGO_DBNAME'] = 'cook'

# # URI of database
app.config['MONGO_URI'] = 'mongodb+srv://recipe_reader:ccwAiFDz5VKmV5dA@cluster0.nayre.mongodb.net/cook?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --

# HOMEPAGE

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
    

# CONNECT TO DB, ADD DATA


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/how_to')
def how_to():
    return render_template('how_to.html')

 
# ________________________________________Routes section API/Learn More________________________________________________________
import requests
url = "https://tripadvisor1.p.rapidapi.com/restaurants/list"


querystring = {"restaurant_tagcategory_standalone":"10591","lunit":"km","restaurant_tagcategory":"10591","limit":"30","currency":"USD","lang":"en_US","location_id":"293919"}

app.config['GIPHY_KEY'] = 'https://tripadvisor1.p.rapidapi.com/restaurants/list'
response = requests.get('https://tripadvisor1.p.rapidapi.com/restaurants/list').json()
querystring = {"restaurant_tagcategory_standalone":"10591","lunit":"km","restaurant_tagcategory":"10591","limit":"30","restaurant_mealtype":"lobster","currency":"USD","lang":"en_US","location_id":"293919"}

headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "a5f304028dmsh7d1413cbfff8d76p13efabjsnf5bba74c75e5"
    }
@app.route('/')
@app.route('/learn_more')
def learn_more():
    return render_template("learn_more.html", time = datetime.now())
@app.route('/restaurant', methods = ['POST', 'GET'])
def restaurant():
    # change the POST to GET 
    if request.method == 'GET':
        mychoice = request.form['restaurantchoice']
        source = requests.request("GET", url, headers=headers, params=querystring)
        return render_template("restaurant.html", time = datetime.now(), source=source)
    else:
        return "error"   

# print(response.text)

# Another function to look for api
#look over the model project

# -- Routes section --
# @app.route('/')
# @app.route('/learn_more')
# def learn_more():
#     return render_template("learn_more.html", time = datetime.now())

# @app.route('/restaurant', methods = ['POST', 'GET'])
# def restaurant():
#     if request.method == 'POST':
#         mychoice = request.form['restaurantchoice']
#         source = requests.get(mychoice, app.config['TRIP_KEY'])
#         return render_template("restaurant.html", time = datetime.now(), source=source)
#     else:
#         return "error"


# ________________________________________Routes section API/Recipes________________________________________________________


recipe_key = 'f72d5cb516fe4796aa7d61932e477990'

@app.route('/recipesearch', methods=['POST', 'GET'])
def search_page():
    
    return render_template('search.html')


# Retrieves a results list of recipes
@app.route('/recipes', methods = ['POST', 'GET'])
def get_recipes():
 
    if request.method == 'POST':
        my_ingr = request.form['ingredients']
        source = getRecipe(fix_query(my_ingr), recipe_key)
        return render_template("found_recipe.html", source=source)
    else:
        return render_template("search_error.html")

# Retrieves specific recipe
@app.route('/<recipe_id>')
def get_recipe(recipe_id):
    recipe_query = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey={recipe_key}"
    response = requests.get(recipe_query).json()
    ingredientsWidget = "recipes/{0}/ingredientWidget".format(recipe_id)
    equipmentWidget = "recipes/{0}/equipmentWidget".format(recipe_id)
    return render_template('recipe.html', recipe=response)

#   recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)

#   recipe_info = requests.request("GET", url + recipe_info_endpoint, headers=headers).json()
    
#   recipe_headers = {
#       'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
#       'x-rapidapi-key': "<6d30ff627cmshb1d1c2c1a6c7772p12ae7bjsn36026cb0df56>",
#       'accept': "text/html"
#   }
#   querystring = {"defaultCss":"true", "showBacklink":"false"}
#   recipe_info['inregdientsWidget'] = requests.request("GET", url + ingedientsWidget, headers=recipe_headers, params=querystring).text
#   recipe_info['equipmentWidget'] = requests.request("GET", url + equipmentWidget, headers=recipe_headers, params=querystring).text
    
  

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
@app.route('/recipehmpg')
def recipehmpg():
    return render_template("recipehmpg.html")
# --------------------------------------Popular Recipes Page------------------------------------------
@app.route('/popularrecipes')
def poprecipe():
    return  render_template("recipehmpg.html")
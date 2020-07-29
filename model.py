import requests

def getRecipe(query, key):
    recipe_query = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={key}&ingredients={query}&number=5"
    response = requests.get(recipe_query).json()
    return response
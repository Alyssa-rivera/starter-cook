import requests

def getRecipe(query, key):
    recipe_query = f"https://api.spoonacular.com/recipes/findByIngredients?{key}ingredients={query}&number=<5>&limitLicense=<false>&ranking=<1>&ignorePantry=<ignorePantry>"
    response = requests.get(recipe_query).json()
    return response
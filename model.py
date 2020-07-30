import requests
import random



# def get(query,key):
#     # pass
#     giphy_query=f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=g&lang=en"
# # change the happy to "query" so user can type 
# # since this function know nothing about key, so do key after query
#     response=requests.get(giphy_query).json()
#     # print(response)
#     return response['data'][random.randint(0,24)]['images']['fixed_height']['url']
def fix_query(query):
    query_fix = query.replace(" ", "+")
    return query_fix

def getRecipe(query_fix, key):
    recipe_query = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={key}&ingredients={query_fix}&number=5"
    response = requests.get(recipe_query).json()
    return response

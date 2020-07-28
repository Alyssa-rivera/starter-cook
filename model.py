# import requests

# def getRecipe(query, key):
#     recipe_query = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=g&lang=en"
#     response = requests.get(recipe_query).json()
#     return response['data'][0]['images']['fixed_height']['url']
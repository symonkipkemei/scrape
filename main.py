import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import rescrape

def store_recipes(url):

    page = rescrape.get_html(url)
    soup = rescrape.get_soup(page)

    recipe_links = rescrape.get_links(soup)

    # store items in dict object
    recipe_store = {}

    for index,link in enumerate(recipe_links,1):
        base_url = "https://codingnomads.github.io/recipes/"
        url = base_url + link
        
        #get recipe items 
        recipe_id = index
        recipe_author = rescrape.get_author(url)
        recipe_title = rescrape.get_title(url)
        recipe_texts = rescrape.get_recipe(url)
        recipe_texts = recipe_texts.split("\n")


        
        recipe_store[recipe_id]= {"recipe_url":url,"recipe_author":{recipe_author},"recipe_title":{recipe_title},"recipe_text":str(recipe_texts)}

        pprint(recipe_store)

    # dict to json
    with open("recipes.json","w") as f:
        json.dump(recipe_store,f)











def main():
    front_url = "https://codingnomads.github.io/recipes/"
    print("Options\n**********************\n1. Collect recipe from the internet \n2. Search for similar recipes\n3. Quit\n**********************")
    
    while True:
        try:
            user_choice  = int(input("select: "))

            if  user_choice == 1:
                scrape(front_url)
            elif user_choice == 2:
                search_recipes()
            elif user_choice == 3:
                break
            else:
                print("Option out of range")
        
        except TypeError:
            print("Select using numbers")

    
if __name__ == "__main__":
    url = "https://codingnomads.github.io/recipes/"
    store_recipes(url)
    




    





        
        
            

    


    


    

   



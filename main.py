import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint


def scrape_recipe_links(front_url:str)-> list:
    """scrape and parse all the recipe links and store in a json file

    Args:
        front_url (str): url for he location of the recipe links

    Returns:
        list: A list of all the recipe urls
    """
    

    # get the page text
    page = requests.get(front_url)

    # create a beautiful soup object
    soup = BeautifulSoup(page.text,"lxml")

    # abstract the links and store in a list
    recipe_links_element = soup.find_all("a")
    recipe_links = [links["href"] for links in recipe_links_element]

    # modify the links by concatenating the front link
    modified_urls = [(front_url + url) for url in recipe_links]

    return modified_urls

def scrape_recipe(recipe_urls:list) -> None:
    """Scrape all the recipe information into a json file

    Args:
        recipe_urls (list): list of all the recipe urls to be scraped
    """

    # store scraped information in a dict
    data = {}
    for URL in recipe_urls:
        # get the recipe page
        page = requests.get(URL)

        # create a soup object to access the html page
        soup = BeautifulSoup(page.text,"lxml")

        # identify author,title,ingredients,instructions and link
        heading = soup.find("h1",class_="title is-2").text
        recipe = soup.find("div",class_="md")


        #filter into unordered list of items(represnets ingredients), If none leave the list empty

        try:
            # generate a list of ingredients
            ingredients = recipe.find("ul")
            ingredients_list = ingredients.find_all("li")
            list_of_ingredients = [ingredient.text for ingredient in ingredients_list]
    
            # generate a list of instructions
            instructions = recipe.find("ol")
            instructions_list = instructions.find_all("li")
            list_of_instructions = [instruction.text for instruction in instructions_list]

        except AttributeError:
            print(f"Incomplete recipe {heading}")
            list_of_instructions = []
            list_of_ingredients = None

        # abstract author name further by removing by 
        by_author = soup.find("p",class_="subtitle is-3 author").text
        author = by_author.strip("by ")

        # store scrapped data in a dictionary
        data[author]={"title":heading,"recipe_url":URL,"ingredients":list_of_ingredients}


    # store the information in a json file
    with open("recipes.json","w") as rp:
        json.dump(data,rp)
        print("Json file with recipes succesfully created")



def name_of_ingredient()-> list:
    """Returms a selected ingredients by the user

    Returns:
        _type_: _description_
    """
    selected_ingredients = []
    try_again = True
    while try_again:
        user_ingredient = input("select an ingredient: ")
        selected_ingredients.append(user_ingredient)
        print(f"ingredients selected: {selected_ingredients}")

        while True:
            user_choice = str.lower(input("insert another(y/n):"))
            if user_choice == "n":
                try_again = False
                break
            elif user_choice == "y":
                try_again= True
                break
            else:
                print("wrong input")

    return selected_ingredients


def fetch_ingredients(user_ingredients:list):
    # unload the data stored in json file

    with open("recipes.json","r") as rp:
        data =json.load(rp)



    # abstract ingredients and name from
    recipes = {recipe["title"]:recipe["ingredients"] for recipe in data.values() if recipe["ingredients"] is not None}

    for ingredient in recipes.values():
        print(ingredient)
        for item in ingredient:
            print(item)





    # abstract recipes only from the list





def main():
    front_url = "https://codingnomads.github.io/recipes/"
    recipe_urls= scrape_recipe_links(front_url=front_url)
    scrape_recipe(recipe_urls)
    
if __name__ == "__main__":
    user = name_of_ingredient()
    fetch_ingredients(user)
    



#

    





        
        
            

    


    


    

   



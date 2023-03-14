import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint



# scrape functions


def get_page_content(front_url):
    # get the page response
    return requests.get(front_url)


def get_html_content(url):
    page = get_page_content(url)
    return page.text

    
def get_soup_object(url):
    html = get_html_content(url)
    # create a beautiful soup object
    soup = BeautifulSoup(html,"lxml")
    return soup



def get_recipe_links(base_url):
    soup = get_soup_object(base_url)

    # abstract the links and store in a list
    recipe_links_element = soup.find_all("a")
    recipe_links = [links["href"] for links in recipe_links_element]

    # modify the links by concatenating the front link
    modified_urls = [(base_url + url) for url in recipe_links]

    return modified_urls


def scrape_recipe(recipe_urls:list) -> dict:
    """Scrape all the recipe information into a dictionary

    Args:
        recipe_urls (list): list of all the recipe urls to be scraped

    Returns:
        dict: a dictionary contianing all the details of the recipe; author,title,recipe-url and list of ingredients
    """
   

    # store scraped information in a dictionary
    data = {}
    #loop through all the links
    for index,URL in enumerate(recipe_urls,1):
        # get the recipe page
        page = requests.get(URL)

        # create a soup object to access the html page
        soup = BeautifulSoup(page.text,"lxml")

        # identify author,title,ingredients,instructions and link
        heading = soup.find("h1",class_="title is-2").text
        recipe = soup.find("div",class_="md")

        # abstract author name further by removing by 
        by_author = soup.find("p",class_="subtitle is-3 author").text
        author = by_author.strip("by ")


        #filter, remain with unordered list of items(represents ingredients), If none leave the list empty

        try:
            # generate a list of ingredients
            ingredients = recipe.find("ul")
            ingredients_list = ingredients.find_all("li")
            list_of_ingredients = [ingredient.text for ingredient in ingredients_list]
    

        except AttributeError:
            print(f"Incomplete recipe: {heading}")
            list_of_ingredients = None

        else:
            # store scrapped data in a dictionary only if ingredients is structured properly
            data[index]={"title":heading,"author":author,"recipe_url":URL,"ingredients":list_of_ingredients}

    return data

def store_recipes(data:dict):
    """Stores the scraped data into a json file

    Args:
        data (dict): recipe information
    """
    try:
        # store the information in a json file
        with open("recipes.json","w") as rp:
            json.dump(data,rp)
            print("Json file with recipes succesfully created")

    except FileNotFoundError:
        print("Keep calm, file is missing....")

def fetch_recipes():
    """Fetch data from the json file
    Returns:
        dict: Returns data 
    """

    with open("recipes.json","r") as rp:
        data =json.load(rp)

    return data

def user_ingredients()-> list:
    """Names of ingredients from the user

    Returns:
        list: a list of ingredients from the user
    """

    selected_ingredients = []

    try:
        user_ingredient = input("select an ingredient: ")
        selected_ingredients.append(user_ingredient)

        while True:
            user_choice = str.lower(input("insert another(y/n):"))
            if user_choice == "n":
                break
            elif user_choice == "y":
                user_ingredient = input("select an ingredient: ")
                selected_ingredients.append(user_ingredient)
            else:
                print("wrong input")

    except ValueError:
        print("You entered a wrong input.")

    return selected_ingredients



# analysis functions

def ingredients_found_in_user(ingr_codingnomads:list,ingr_user:list)-> tuple:
    """ Search for user ingredients in codingnomads recipe list, if available gives it a score

    Args:
        ingr_codingnomads (list): A list of ingredients provided by codingnomads
        ingr_user (list): user list of requirments

    Returns:
        tuple:the number of user ingredients found
    """

    score = 0
    out_of = len(ingr_user)

    #return the score of recipes found over the total 
    for ingredient in ingr_user:
        for recipe_ingr in ingr_codingnomads:
            index_ingr = recipe_ingr.find(ingredient)

            if index_ingr != -1:
                score += 1


    return score


def fetch_match_ingredients(data:dict, user_ingredients:list):
    match_recipes = {}

    for recipe in data.values():
        title = recipe["title"]
        author = recipe["author"]
        url = recipe["recipe_url"]
        ingr = recipe["ingredients"]


        score = ingredients_found_in_user(ingr,user_ingredients)

        if score > 0:
            match_recipes[title] = score

    return match_recipes


# compiler functions

def scrape(front_url):
    """scrape information from the database"""
    front_url = "https://codingnomads.github.io/recipes/"
    recipe_urls= get_recipe_links(front_url=front_url)
    data = scrape_recipe(recipe_urls)
    store_recipes(data)


def search_recipes():
    user_ingr = user_ingredients()
    data = fetch_recipes()
    match_recipes = fetch_match_ingredients(data,user_ingr )
    
    for recipe,score in match_recipes.items():
        print(f"{recipe}:{score}")


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
    soup = get_recipe_links(url)
    print(type(soup))

    




    





        
        
            

    


    


    

   



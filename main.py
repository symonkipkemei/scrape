import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import rescrape
import os
import sqlalchemy as s

# connecting to the database
database_password = os.environ["PY_MYSQL"]
database_name = "recipe"


#get connections
engine = s.create_engine(f"mysql+pymysql://root:{database_password}@localhost/{database_name}")
connection = engine.connect()
metadata = s.MetaData()


#get the table
table = s.Table("recipe",metadata,autoload=True,autoload_with=engine)

def store_recipes(url):

    page = rescrape.get_html(url)
    soup = rescrape.get_soup(page)

    recipe_links = rescrape.get_links(soup)

    # store items in dict object
    recipe_store = []

    for link in recipe_links:
        base_url = "https://codingnomads.github.io/recipes/"
        
        #get recipe items 
        recipe_url = url = base_url + link
        recipe_author = rescrape.get_author(url)
        recipe_title = rescrape.get_title(url)
        recipe_texts = rescrape.get_recipe(url)

        #store them in the list object
        data = {"recipe_url":recipe_url,"recipe_author":recipe_author,"recipe_texts":recipe_texts,"recipe_title":recipe_title}
        recipe_store.append(data)

        print(f"Data fetched from {recipe_url}>>>>>>>>")

    
    return recipe_store


def insert_database(data:dict):

    for index,file in enumerate(data,1):
        #abstract the values to be inserted into database and map them into their respective column names and insert to database

        insert = s.insert(table).values(
            recipe_author = file["recipe_author"],
            recipe_title = file["recipe_title"],
            recipe_texts  = file["recipe_texts"],
            recipe_url = file["recipe_url"]
            )
        
        proxy = connection.execute(insert)
        
        print(f"File url: {index} inserted successfully")


def main():
    pass

if __name__ == "__main__":
    url = "https://codingnomads.github.io/recipes/"
    data = store_recipes(url)
    insert_database(data)





    
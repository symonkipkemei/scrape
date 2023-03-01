import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint


def scrape_links(front_url):
    """scrape and parse all the recipe links
    """

    # get the page text
    page = requests.get(front_url)

    # create a beautiful soup object
    soup = BeautifulSoup(page.text)

    # abstract the links and store in a list
    recipe_links_element = soup.find_all("a")
    recipe_links = [links["href"] for links in recipe_links_element]

    return recipe_links


def recipe_details(front_url,urls:list):
    # modify the links by concatenating the front link
    modified_urls = [(front_url + url) for url in urls]

    # store data in a  dictionary /list
    recipe = {}

    for URL in modified_urls:
        # get the recipe page
        page = requests.get(URL)

        # create a soup object to access the html page
        soup = BeautifulSoup(page.text)

        # find author,title and recipe objects
        author_obj = soup.find("p", class_="author")
        title_obj = soup.find("h1",class_="title is-2")
 

        author = author_obj.text.strip("by")
        title = title_obj.text
    
        recipe[author] = {"title":(title)}
        
    # store the information in a json file

    with open("recipes.json","w") as rp:
        json.dump(recipe,rp)
        print("Json file succefully created")



        
def main():
    front_url = "https://codingnomads.github.io/recipes/"
    recipe_links = scrape_links(front_url=front_url)
    recipe_details(front_url,recipe_links)

 
if __name__ == "__main__":
    main()

        
        
            

    


    


    

   



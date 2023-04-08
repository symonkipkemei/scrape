
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_page(url:str) -> requests.Response:
    """Get response from the page

    Args:
        url (str): the url to the page

    Returns:
        requests.Response: The Response object
    """
    response = requests.get(url)
    return response


def get_html(url:str):
    """get html from the response

    Args:
        url (str): Url to the website

    Returns:
        _type_: html response
    """
    page = get_page(url)
    return page.text


def get_soup(html) -> BeautifulSoup:
    """convert the html response to an object

    Args:
        html (_type_): html response

    Returns:
        BeautifulSoup: Beautifuls soup object
    """
    soup = BeautifulSoup(html,"lxml")
    return soup

def get_links(soup:BeautifulSoup) -> list:
    """Abstract all the links in the front page

    Args:
        soup (BeautifulSoup): The soup object

    Returns:
        list: List of all the recipe links
    """

    # abstract the links and store in a list
    content = soup.find("div", class_="content is-normal")
    lists = content.find_all("li")
    links = [list.find("a").get("href") for list in lists]

    return links
    

def get_author(url:str) -> str:
    """Get the author name from the particular page

    Args:
        url (str): url to the recipe page

    Returns:
        str: the name of the author
    """
    
    html = get_html(url)
    soup = get_soup(html)
    author = soup.find("p",class_="subtitle is-3 author").text
    #remove by
    author_by_name = author.split(" ")
    author_name = author_by_name[1]
    return author_name

def get_title(url:str) -> str:
    """Get the title from the particular page

    Args:
        url (str): url to the recipe page

    Returns:
        str: title of the recipe
    """
    html = get_html(url)
    soup = get_soup(html)
    title = soup.find("h1",class_="title is-2").text
    return title



def get_recipe(url:str) -> str:
    """Get the recipe from the particular page

    Args:
        url (str):url to the recipe page

    Returns:
        str: the recipe text
    """
    html = get_html(url)
    soup = get_soup(html)
    recipe = soup.find("div",class_="md").text
    return recipe



if __name__ == "__main__":
    base_url = "https://codingnomads.github.io/recipes/"
    html = get_html(base_url)
    soup = get_soup(html)
    pprint(get_links(soup))



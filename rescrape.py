


import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_page(url):
    response = requests.get(url)
    return response


def get_html(url):
    page = get_page(url)
    return page.text


def get_soup(html):
    soup = BeautifulSoup(html,"lxml")
    return soup

def get_links(soup):

    # abstract the links and store in a list
    content = soup.find("div", class_="content is-normal")
    lists = content.find_all("li")
    links = [list.find("a").get("href") for list in lists]

    return links
    

def get_author(url):
    html = get_html(url)
    soup = get_soup(html)
    author = soup.find("p",class_="subtitle is-3 author").text
    #remove by
    author_by_name = author.split(" ")
    author_name = author_by_name[1]
    return author_name

def get_title(url):
    html = get_html(url)
    soup = get_soup(html)
    title = soup.find("h1",class_="title is-2").text
    return title



def get_recipe(url):
    html = get_html(url)
    soup = get_soup(html)
    recipe = soup.find("div",class_="md").text
    return recipe



if __name__ == "__main__":
    base_url = "https://codingnomads.github.io/recipes/"
    html = get_html(base_url)
    soup = get_soup(html)
    pprint(get_links(soup))



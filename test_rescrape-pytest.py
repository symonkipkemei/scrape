import rescrape


BASE_URL = "https://codingnomads.github.io/recipes/"
sample_url = "https://codingnomads.github.io/recipes/recipes/0-i-m-working-on-movin.html"

def test_get_page():
    assert rescrape.get_page(BASE_URL).status_code == 200
    assert rescrape.get_page(sample_url).status_code == 200

def test_get_html():
    assert "<!DOCTYPE html>" in rescrape.get_html(BASE_URL)

def test_get_soup():
    html = rescrape.get_html(BASE_URL)
    soup =rescrape.get_soup(html)
    assert "<class 'bs4.BeautifulSoup'>" == str(type(soup))

def test_get_links():
    html = rescrape.get_html(BASE_URL)
    soup =rescrape.get_soup(html)
    links = rescrape.get_links(soup)
    assert len(links) != 0

def test_get_author():
    assert rescrape.get_author(sample_url) == "mrfish1991"

def test_get_title():
    assert rescrape.get_title(sample_url) == "I'm working on moving all my mothers hand written recipes into a digital cookbook. Would you guys like to have it when its done? Or maybe some of my favorites?"


def test_get_recipe():
    assert type(rescrape.get_recipe(sample_url)) is str
    assert len(rescrape.get_recipe(sample_url)) != 0
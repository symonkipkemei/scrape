
import unittest
import rescrape

class TestRescrape(unittest.TestCase):

    def setUp(self) -> None:
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.sample_url = "https://codingnomads.github.io/recipes/recipes/5-mini-brownie-trifles.html"

    #get page
    def test_get_page(self):
        self.assertEqual(rescrape.get_page(self.BASE_URL).status_code,200)

    # get the html content
    def test_get_html(self):
        self.assertIn("<!DOCTYPE html>",rescrape.get_html(self.BASE_URL))

    #get the soup object
    def test_get_soup(self):
        html = rescrape.get_html(self.BASE_URL)
        self.assertEqual("<class 'bs4.BeautifulSoup'>",str(type((rescrape.get_soup(html)))))
    
        
    #get the links
    def test_get_links(self):
        html = rescrape.get_html(self.BASE_URL)
        soup = rescrape.get_soup(html)
        self.assertNotEqual(len(rescrape.get_links(soup)),0)
        


    #get author
    def test_get_author(self):
        self.assertEqual(rescrape.get_author(self.sample_url),"reddituser246")
        self.assertNotEqual(len(rescrape.get_author(self.sample_url)), 0)

    #get title
    def test_get_title(self):
        self.assertEqual(rescrape.get_title(self.sample_url),"Mini brownie trifles")

    #get recipe text
    def test_get_recipe(self):
        self.assertIsInstance(rescrape.get_recipe(self.sample_url),str)
        self.assertGreater(len(rescrape.get_recipe(self.sample_url)),0)



if __name__ == "__main__":
    unittest.main()

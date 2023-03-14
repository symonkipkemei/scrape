import unittest
import main
from bs4 import BeautifulSoup


class TestMain(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.url = f"{self.BASE_URL}recipes/11-making-my-own-baguet.html"
        

    # request can establish a connection and recieve a valid request

    def test_get_page_content_returns_valid_response(self):
        index_page = main.get_page_content(self.BASE_URL)
        self.assertEqual(index_page.status_code,200)

    def test_get_html_content_returns_html_string(self):
        page = main.get_html_content(self.BASE_URL)
        self.assertIn("<!DOCTYPE html>", page)

    def test_get_soup_object_returns_class_bs4(self):
        soup = main.get_soup_object(self.BASE_URL)
        self.assertEqual("<class 'bs4.BeautifulSoup'>",str(type(soup)))

    def test_get_recipe_links_returns_list_of_recipe_links(self):
        recipe_links = main.get_recipe_links(self.BASE_URL)
        self.assertEqual("<class 'list'>",str(type(recipe_links)))
 



    #can identify links from all t

    def test_get_ingredients_found_in_user(self):
        self.assertEqual(main.ingredients_found_in_user([" a book mangoes in", "mangoes ripe", "sugar has expired","tasty salt"],["salt","mangoes"]),2)


if __name__ == "__main__":
    unittest.main()
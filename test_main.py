import unittest
import main
from bs4 import BeautifulSoup


class TestMain(unittest.TestCase):

    # request can establish a connection and recieve a valid request

    def test_get_valid_html_response(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        index_page = main.get_page_content(BASE_URL)
        self.assertEqual(index_page.status_code,200)

    def test_reponse_contains_html_code(self):
        page = main.get_page_content("https://codingnomads.github.io/recipes/")
        ans = main.html_code_availability(page)
        self.assertTrue(ans,True)

    def test_check_html_to_soup_object_conversion(self):
        page = main.get_page_content("https://codingnomads.github.io/recipes/")
        soup = main.html_to_soup(page)
        soup_type= type(soup)
        pass

    #the html can be successfully converteed to beautiful soup object


    #can identify links from all t

    def test_get_ingredients_found_in_user(self):
        self.assertEqual(main.ingredients_found_in_user([" a book mangoes in", "mangoes ripe", "sugar has expired","tasty salt"],["salt","mangoes"]),2)


if __name__ == "__main__":
    unittest.main()
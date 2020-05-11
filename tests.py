import unittest
import main
from unittest import TestCase
from unittest.mock import patch
import parsing as script
import pytest

result = main.select_wiki_article(57644)
class TestMain(unittest.TestCase):
    def test_select_wiki_article(self):
        response = main.select_wiki_article(page=57644)
        self.assertTrue(response, result)

    def test_search_wiki_articles(self):
        main.search_wiki_articles('Sofia')
        self.assertIsNotNone(dict)

    @patch('main.get_random_page')
    def test_get_random_page(self, MockRandomPage):
        Random_page = MockRandomPage()

        Random_page.posts.return_value = [
            {
                'search': 'Sofia',
                'pageid': 57644,
                'title': 'Sofia',
                'extract': 'Sofia is the capital of Bulgaria'
            }
        ]

        response = Random_page.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)


class TestParser:

    user_query = script.Pars('Bonjour GrandPy! Tu peux me donner l\'adresse du Louvre?')

    def test_get_text(self):
        # input in lowercase
        print(self.user_query.textinput)
        assert self.user_query.textinput == 'bonjour grandpy! tu peux me donner l\'adresse du louvre?'


    def test_delete_input_of_symbols(self):
        #testing the method that delete all Alpha symbols
        self.user_query.delete_input_of_symbols()
        print(self.user_query.textinput)
        assert self.user_query.textinput == 'bonjour grandpy tu peux me donner ladresse du louvre'

    def test_delete_input_of_stopwords(self):
        #testing themethod that removes all stopwords
        # self.test_delete_input_of_symbols()
        self.user_query.delete_input_of_stopwords()
        assert self.user_query.final_query_in_string != 'bonjour'

    def test_textinput_type(self):
        # cheking the tipy of our input
        assert isinstance(self.user_query.textinput, str)

if __name__== "__main__":
    unittest.main()
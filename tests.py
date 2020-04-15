import unittest
import main
from unittest import TestCase
from unittest.mock import patch

class TestMain(unittest.TestCase):
    def test_select_wiki_article(self):
        response = main.select_wiki_article(page=57644)
        self.assertTrue(response, dict)

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

if __name__== "__main__":
    unittest.main()
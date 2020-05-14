import main
import tests
print('---------------------------Information about search_wiki_articles-----------------------------------')

print(main.search_wiki_articles('Sofia')) # i'm passing a city of New York for verifying if my wiki_search_params works correctly

print('-------------------------Information about select_wiki_article--------------------------------------')

print(main.select_wiki_article(57644)) # i passed this number who correspond of New York pageids and i recived back the ['extract'] about my page and the article_url link, so that means my return statement workl correctly

print('----------------------------------------------------------------------------------------------------')


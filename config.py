GOOGLE_MAPS_API = {
    'URL': 'https://www.google.com/maps/embed/v1/place',
    'KEY': '*******'  # YOUR_GOOGLE_API_KEY
}

WIKI_API = {
    'ARTICLE_URL': 'https://en.wikipedia.org/wiki/',
    'SEARCH_REQUEST': {
        'URL': 'https://en.wikipedia.org/w/api.php',
        'PARAMS': {
            'action': 'query',
            'format': 'json',
            'list': 'search'
        }
    },
    'SELECT_REQUEST': {
        'URL': 'https://en.wikipedia.org/w/api.php',
        'PARAMS': {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exlimit': 1,
            'explaintext': True,
            'exsectionformat': 'plain',
            'exintro': True
        }
    }
}

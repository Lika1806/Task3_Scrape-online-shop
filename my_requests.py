import requests

def get_text(url,*, keep_trying = False, attempts=5):
    """Retrieves text content from a given URL
    Returns text content of the response if it's successful, otherwise returns None
    If keep_trying is set to True, the function will keep trying the request 
    until it succeeds or until the maximum number of attempts is reached."""
    if not keep_trying:
        attempts = 1
    while attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(e)
        attempts-=1
    return None

if __name__== '__main__':

    url_working = 'https://en.wikipedia.org/wiki/List_of_Armenian_architects'
    url_not_found = 'https://en.wikipedia.org/wiki/List_of_Armenian_architects5'
    url_random_response = 'https://httpstat.us/Random/200,201,500-504'
    
    #using working url
    print(get_text(url_working)[:50]+'......\n')

    #using page url that doesn't exist
    print(get_text(url_not_found))

    #using page url with random response for test
    get_text(url_random_response)

    #using page url with random response whith several tries
    print(get_text(url_random_response,keep_trying=True))
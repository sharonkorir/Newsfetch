
import urllib.request, json
from .models import Source, Article

#get api key
api_key = None

#get news source url
base_url = None
article_url = None

def configure_request(app):
   global api_key, base_url, article_url
   api_key = app.config['NEWS_API_KEY']
   base_url = app.config['NEWS_API_SOURCE_URL']
   article_url = app.config['NEWS_API_ARTICLES_URL']

def get_sources():
    '''
    Function that gets the json response to the url request
    '''
    get_sources_url = base_url.format(api_key)
    #print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    processes the source results and transforms them to a list of objects
    
    Args: 
        source_list: a list of dictionaries that contain news source details
    Returns:
        source_results: a list of news source objects 
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        #article_results = get_articles(id)
        
        source_object = Source(id, name, description, url)
        source_results.append(source_object)

    
    return source_results

def get_articles(id):
    get_articles_url = article_url.format(id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        article_data = url.read()
        article_data_response = json.loads(article_data)

        article_results = None

        if article_data_response['articles']:
            article_list = article_data_response['articles']
            article_results = process_articles_results(article_list)
        
        print("test", article_results, id)
        return article_results

def process_articles_results(article_list):
    
    article_results = []

    for article_item in article_list:
        title = article_item.get('title')
        image = article_item.get('urlToImage')
        description = article_item.get('description')
        url = article_item.get('url')
        time = article_item.get('publishedAt')
        source = article_item.get('source.name')

        article_object = Article(source, title, description, url, image, time)
        article_results.append(article_object)
        print("test article", article_object.description)

    #print("test", article_item)
    return article_results

def search_article(article_title):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article_title, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        article_data = url.read()
        article_data_response = json.loads(article_data)

        search_article_results = None

        if article_data_response['articles']:
            search_article_list = article_data_response['articles']
            search_article_results = process_articles_results(search_article_list)
            
    return search_article_results
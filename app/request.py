from app import app
import urllib.request, json
from .models import news_sources

Source = news_sources.Source

#get api key
api_key = app.config['NEWS_API_KEY']

#get news source url
base_url = app.config["NEWS_API_SOURCE_URL"]
#base_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=cb57bf9b6162483bba03f1cbc7be3e87'

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

        source_object = Source(id, name, description, url)
        source_results.append(source_object)

    return source_results

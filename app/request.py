from app import app
import urllib.request, json
from .models import news_articles, news_sources

#get api key
api_key = app.config['NEWS_API_KEY']

#get news source url
source_url = app.config["NEWS_API_SOURCE_URL"]

def get_sources(source):
    '''
    Function that gets the json response to the url request
    '''
    get_sources_url = source_url.format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    '''
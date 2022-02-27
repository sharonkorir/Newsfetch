import os

from instance.config import NEWS_API_KEY

class Config:
    ''''
    general configuration parent class
    '''
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    production configuration child class
    
    args:
        Config: the parent configuration class with general configuraton settings
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    
    args:
        Config: the parent configuration class with general configuraton settings
    '''
    
    DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}
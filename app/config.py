class Config:
    ''''
    general configuration parent class
    '''
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    
    #NEWS_API_ARTICLES_URL = ''

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
class Config:
    ''''
    general configuration parent class
    '''
    pass

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
class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_ARTICLE_API_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    # SOURCE_ARTICLE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=80ec86b4b19148579a64f273b9f5a047'
    
class ProdConfig(Config):

    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
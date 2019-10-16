import urllib.request
import json
from .models import News
from .models import Articles

# News = news.News
# Article = article.Articles


# Getting api key
apikey = None
# Getting the movie base url
base_url = None
article_url = None

def configure_request(app):
    global apikey,base_url,article_url
    apikey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config ['NEWS_ARTICLE_API_URL']
# apikey = app.config['NEWS_API_KEY']
# Getting the news base url
# base_url = app.config["NEWS_API_BASE_URL"]
# article_url = app.config ["NEWS_ARTICLE_API_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,apikey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    '''

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name= news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        if name:
            news_object = News(id,name,description,url,category,country)
            news_results.append(news_object)

    return news_results

def get_articles(article):

    get_article_url = article_url.format(article,apikey)
    print(get_article_url)

    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_result = None

        if article_response['articles']:
            article_response_list = article_response['articles']
            article_result = process_new_article(article_response_list)

    return article_result

def process_new_article(article_list):
    article_result = []

    for  article_item in article_list :
        title = article_item.get('title')
        author = article_item.get('author')
        source = article_item.get('source')
        name = article_item.get('name')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        new_article = Articles(title,author,source,name,description,url,urlToImage,publishedAt)
        article_result.append(new_article)
        
    return article_result


def article_source(source):
    sources_url =article_url.format(source,apikey)

    with urllib.request.urlopen(sources_url) as url:
        art_data = url.read()
        response = json.loads(art_data)

        source_article =  None

        if response['articles']:
            source_article_list = response['articles']
            source_article = process_article_source(source_article_list)

    return source_article

def process_article_source(article_list):
    article_source = []

    for one_art in article_list:
        source = one_art.get('source')
        name = one_art.get('name')
        author = one_art.get('author')
        title = one_art.get('title')
        description = one_art.get('description')
        url = one_art.get('url')
        urlToImage = one_art.get('urlToImage')
        publishedAt = one_art.get('publishedAt')


        article_object = Articles(source,name,author,title,description,url,urlToImage,publishedAt)
        article_source.append(article_object)

    return article_source

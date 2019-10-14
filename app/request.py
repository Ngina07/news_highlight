from app import app
import urllib.request
import json
from .models import news
from .models import articles

News = news.News
Articles = articles.Articles

#Getting apikey

apikey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
article_url = app.config ["NEWS_ARTICLE_API_URL"]


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(apikey)

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

def get_article(Articles):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_url.format(apikey)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['sources']:
            article_results_list = get_article_response['sources']
            article_results = process_article_results(article_results_list)
    return article_results


def process_article_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    '''

    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name= article_item.get('name')
        description = article_item.get('description')
        url = article_item.get('url')
        category = article_item.get('category')
        language = article_item.get('language')

        if name:
            news_object = News(id,name,description,url,category,language)
            article_results.append(news_object)

    return article_results


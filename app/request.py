from app import app
import urllib.request
import json
from models import NEWS_API_KEY

News = news.News

#Getting apikey

api_key = app.config['NEWS_API_KEY ']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base.url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
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
        url = news_item.get('url_path')
        category = news_item.get('category')
        country = news_item.get('country')

        if url:
            news_object = news(id,name,description,url,category,country)
            news_results.append(news_object)

    return news_results
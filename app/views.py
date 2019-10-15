from flask import render_template
from app import app
from .request import get_news
from .request import get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting news name list
    # popular_news = get_news()
    gene_news = get_news('general')
    business_news = get_news('business')
    sport_news = get_news('sports')
    # print(popular_news)
    # title = 'Welcome to the Best News Site in the region'
    return render_template('index.html',general = gene_news,business =business_news,sports=sport_news )

#Displays news sources to home page

@app.route('/articles/<id>')
def sourceArticle(id):
    '''
    Views thats renders news sources to the home page
    '''
    all_articles = get_articles(id)
    print(all_articles)
    source = id
    return render_template('article.html', articles = all_articles, source = source)
    

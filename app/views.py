from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting news name list
    popular_news = get_news()
    print(popular_news)
    title = 'Welcome to the Best News Site in the region'
    return render_template('index.html', title = title,name_news = popular_news)


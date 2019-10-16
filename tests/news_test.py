import unittest
from app.models import News

News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Run helter skelter','Everybody ran helter skelter','https://image.tmdb.org/t/p/w500/khsjha27hbs','Breaking News','United States')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


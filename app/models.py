class News: #class for sources
    '''
    News class to define news objects
    '''
    def __init__(self,id,name, description, url, category, country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    '''
    A class that defines the article object
    '''
    def __init__(self,source,name,author,title,description,url,urlToImage,publishedAt):
        self.source = source
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
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

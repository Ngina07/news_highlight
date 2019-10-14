class Articles:  #Class for articles
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,name, description,url, category, language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url 

class Article:
    '''
    Source class to define Source Objects
    '''

    def __init__(self, source_id, title, description, url, image, time):
        self.source_id = source_id
        self.title = title
        self.description = description
        self.article_url = url 
        self.image = image
        self.time = time
  

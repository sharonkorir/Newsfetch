class Article:
    '''
    Source class to define Source Objects
    '''

    def __init__(self, source_id, title, description, url, image, time):
        self.source_id = source_id
        self.title = title
        self.description = description
        self.artcle_url = url 
        self.image = image
        self.time = time
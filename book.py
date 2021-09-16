class Book:
    def __init__(self, title:str=None, author:str=None, rating:int=None, user:User=None):
        self.title = title
        self.author = author
        self.rating = rating
        self.user = user
    
    
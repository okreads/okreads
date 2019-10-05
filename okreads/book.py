class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def to_dict(self):
        return {'isbn': self.isbn, 'title': self.title, 'author': self.author}

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    @staticmethod
    def from_dict(data: dict):
        return Book('', data['title'], data['authors'][0]['author']['key'])

    def to_dict(self):
        return {'isbn': self.isbn, 'title': self.title, 'author': self.author}

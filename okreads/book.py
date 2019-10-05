from okreads.db import Db


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


class BookRepository:
    def getById(self, id) -> Book:
        book = Db.fetchAll(f'SELECT * FROM book where id={id};')
        return self._mapToEntity(book[0])

    def getAll(self, limit=100):
        books = Db.fetchAll(f'SELECT * FROM book LIMIT {limit};')
        return list(map(self._mapToEntity, books))

    def _mapToEntity(self, data):
        return Book(isbn=data[1], title=data[2], author=data[0])

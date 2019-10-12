from okreads.db import Db
import json
import sys


class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def to_dict(self):
        return {'isbn': self.isbn, 'title': self.title, 'author': self.author}


class BookRepository:
    def save(self, book: Book):
        Db.execute('insert into book (title, author) values (:title, :author)', {
            'title': book.title,
            'author': book.author
        })

    def getById(self, id) -> Book:
        book = Db.fetchAll(f'SELECT * FROM book where id={id};')
        return self._mapToEntity(book.first())

    def getAll(self, limit=3):
        books = Db.fetchAll(f'SELECT * FROM book LIMIT {limit};')
        return list(map(self._mapToEntity, books))

    def _mapToEntity(self, data):
        return Book(isbn=data[1], title=data[2], author=data[0])

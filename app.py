from flask import Flask
from flask import jsonify
from okreads.book import Book
from okreads.db import Db

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/books')
def books():
    repository = BookRepository()
    result = repository.getAll(10)
    return jsonify({'books': result})

def book():
    repository = BookRepository()
    result = repository.getById('10')
    return jsonify({'books': [result]})

class BookRepository:
    def getById(self, id)->Book:
      book = Db.fetchAll(f'SELECT * FROM book where id={id};')
      return self._mapToEntity(book)
    def getAll(self, limit=100):
      books = Db.fetchAll(f'SELECT * FROM book;')
      return list(map(self._mapToEntity, books))
    def _mapToEntity(self, data):
      return Book(data.get('isbn', None), data.get('title', None), data.get('author', None))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

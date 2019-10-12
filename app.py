from flask import Flask
from flask import jsonify
from okreads.book import Book, BookRepository
from okreads.db import Db

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello reads!"


@app.route('/books')
def books():
    repository = BookRepository()
    result = list(map(lambda x: x.to_dict(), repository.getAll(10)))
    return jsonify({'books': result})


@app.route('/book/<int:book_id>')
def book(book_id):
    repository = BookRepository()
    result = repository.getById(book_id)
    return jsonify({'book': result.to_dict()})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

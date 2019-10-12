from flask import Flask, jsonify, Blueprint, render_template
from okreads.book import Book, BookRepository
from okreads.db import Db
from okreads.author import AuthorRepository

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello reads!"


@app.route('/api/books')
def books():
    repository = BookRepository()
    result = list(map(lambda x: x.to_dict(), repository.getAll()))
    return jsonify({'books': result})


@app.route('/api/book/<int:book_id>')
def book(book_id):
    repository = BookRepository()
    result = repository.getById(book_id)
    return jsonify({'book': result.to_dict()})


ui = Blueprint('ui', __name__, static_folder='okreads/static/', template_folder='okreads/template/')


@ui.route('/author/<int:author_id>', methods=['GET'])
def author_details_page(author_id):
    repository = AuthorRepository()
    author = repository.getById(author_id)
    return jsonify(author.to_dict())


@ui.route('/book/<int:book_id>', methods=['GET'])
def book_details_page(book_id):
    repository = BookRepository()
    book = repository.getById(book_id)
    return render_template('book.html', book=book.to_dict())


app.register_blueprint(ui, url_prefix='/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

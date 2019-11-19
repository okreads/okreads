from flask import Flask, jsonify, Blueprint, render_template
from okreads.book import Book, BookRepository
from okreads.db import Db
from okreads.author import AuthorRepository

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello reads!"

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.debug = True
    app.run(host='0.0.0.0')

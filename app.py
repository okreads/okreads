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

    result = Db.fetchAll("SELECT * FROM book LIMIT=10;")

    return jsonify({'books': [result]})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

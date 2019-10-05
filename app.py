from flask import Flask
from flask import jsonify
from okreads.book import Book

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/books')
def books():

    book1 = Book(123, 'harry potter', 'rowlling')
    book2 = Book(321, 'harry potter 2', 'rowlling')

    return jsonify({'books': [book1.to_dict(), book2.to_dict()]})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

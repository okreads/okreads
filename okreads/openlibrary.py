from okreads.author import Author, AuthorRepository
from okreads.book import Book, BookRepository
import json


def import_author(single_author_data: dict):

    data = json.loads(single_author_data)
    author = Author(data['name'], data.get('bio.value', ""), data.get('location', ''),
                    data.get('birth_date', ""), data.get('death_date', ""),
                    data.get('wikipedia', ""), data['key'])

    AuthorRepository().save(author)


def import_book(single_book_data: dict):
    data = json.loads(single_book_data)

    book = Book('', data['title'], data['authors'][0]['author']['key'])
    BookRepository().save(book)

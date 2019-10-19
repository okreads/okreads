from okreads.author import Author, AuthorRepository
from okreads.book import Book, BookRepository
import json


def import_author(single_author_data: dict):

    data = json.loads(single_author_data)
    open_library_id = data['key']
    author = Author(data.get('name'), data.get('bio.value', ""), data.get('location', ''),
                    data.get('birth_date', ""), data.get('death_date', ""),
                    data.get('wikipedia', ""), open_library_id)

    database_author = AuthorRepository().findByOpenLibraryId(open_library_id)
    if database_author:
        author.id = database_author.id
        AuthorRepository().update(author)
    else:
        AuthorRepository().create(author)


def import_book(single_book_data: dict):
    data = json.loads(single_book_data)

    book = Book('', data['title'], data['authors'][0]['author']['key'])
    BookRepository().save(book)

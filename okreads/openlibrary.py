from okreads.author import Author, AuthorRepository
import json


def import_author(single_author_data: dict):

    data = json.loads(single_author_data)
    author = Author(data['name'], data.get('bio.value', ""), data.get('location', ''),
                    data.get('birth_date', ""), data.get('death_date', ""),
                    data.get('wikipedia', ""))

    AuthorRepository().save(author)

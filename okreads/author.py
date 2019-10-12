from okreads.db import Db
import json


class Author:
    def __init__(self, name, bio, location, birth_date, death_date, wikipedia_link, open_library_id):
        self.name = name
        self.bio = bio
        self.location = location
        self.birth_date = birth_date
        self.death_date = death_date
        self.wikipedia_link = wikipedia_link
        self.open_library_id = open_library_id

    def to_dict(self):
        return self.__dict__


class AuthorRepository:
    def save(self, author: Author):
        Db.execute('insert into author (info, open_library_id ) values (:info, :open_library_id)',
                   {"info": json.dumps(author.to_dict()), "open_library_id": author.open_library_id})

    def getById(self, id) -> Author:
        author = Db.fetchAll(f'SELECT * FROM author where id={id};')
        return self._mapToEntity(author.first()['info'])

    def _mapToEntity(self, data):
        return Author(name=data["name"], bio=data["bio"], location=data["location"], birth_date=data['birth_date'], death_date=data['death_date'], wikipedia_link=data['wikipedia_link'], open_library_id=data['open_library_id'])
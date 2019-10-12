from okreads.db import Db
import json


class Author:
    def __init__(self, name, bio, location, birth_date, death_date, wikipedia_link):
        self.name = name
        self.bio = bio
        self.location = location
        self.birth_date = birth_date
        self.death_date = death_date
        self.wikipedia_link = wikipedia_link

    def to_dict(self):
        return self.__dict__


class AuthorRepository:
    def save(self, author: Author):
        Db.execute('insert into author (info) values (:info)',
                   {"info": json.dumps(author.to_dict())})

    def getById(self, id) -> Author:
        author = Db.fetchAll(f'SELECT * FROM author where id={id};')
        return author.first()

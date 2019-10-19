from okreads.db import Db
from typing import Optional
import json


class Author:
    def __init__(self,
                 name="Unknown",
                 bio=None,
                 location=None,
                 birth_date=None,
                 death_date=None,
                 wikipedia_link=None,
                 id=None,
                 open_library_id=None):
        self.name = name
        self.bio = bio
        self.location = location
        self.birth_date = birth_date
        self.death_date = death_date
        self.wikipedia_link = wikipedia_link
        self.id = id
        self.open_library_id = open_library_id

    def to_dict(self):
        return self.__dict__


class AuthorRepository:
    def create(self, author: Author):
        Db.execute('insert into author (info, open_library_id ) values (:info, :open_library_id)', {
            "info": json.dumps(author.to_dict()),
            "open_library_id": author.open_library_id
        })

    def update(self, author: Author):
        Db.execute('update author set info = (:info) where open_library_id = :open_library_id', {
            "info": json.dumps(author.to_dict()),
            "open_library_id": author.open_library_id
        })

    def getById(self, id) -> Author:
        author = Db.fetchAll(f'SELECT * FROM author where id=:id;', {'id': id})
        return self._mapToEntity(author.first())

    def findByOpenLibraryId(self, id) -> Optional[Author]:
        author = Db.fetchAll(
            f'SELECT id, info, open_library_id FROM author where open_library_id=:id;', {'id': id})
        data = author.first()
        if data is None:
            return None

        return self._mapToEntity(data)

    def _mapToEntity(self, data):
        author = Author(name=data['info']["name"],
                        bio=data['info']["bio"],
                        location=data['info']["location"],
                        birth_date=data['info']['birth_date'],
                        death_date=data['info']['death_date'],
                        wikipedia_link=data['info']['wikipedia_link'],
                        id=data['id'],
                        open_library_id=data['open_library_id'])

        return author

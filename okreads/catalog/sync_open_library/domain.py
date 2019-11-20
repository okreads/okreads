from typing import NamedTuple, Any, Callable, NewType, Generator, Optional
import os
# public interface
# @todo create command generic type

WorkflowInterface = Callable[['SyncOpenLibraryCmd'], 'BookPersistedEvents']

SyncOpenLibraryCmd = NamedTuple('SyncOpenLibraryCmd', [('filename', str), ('limit', Optional[int])])
BookPersistedEvents = Generator['BookPersistedEvent', None, None]
BookPersistedEvent = NamedTuple('BookPersistedEvent', [('persisted_book_data', 'PersistedBookData')])

# private interface

OpenLibraryBookReference = NewType('OpenLibraryBookReference', str)
BookReferences = Generator[OpenLibraryBookReference, None, None]


LoadOpenLibraryBookReference = Callable[['ExistingFile', Optional['LinesToLoadLimit']], BookReferences]
UnvalidatedBookData = NamedTuple('UnvalidatedBookData', [('author_data', Any), ('title', str)])
LoadOpenLibraryBookData = Callable[[OpenLibraryBookReference], UnvalidatedBookData]

PersistedBookData = NewType('PersistedBookData', 'ValidatedBookData')

PersistBook = Callable[['ValidatedBookData'], PersistedBookData]


class ValidatedBookData:
    def __init__(self, data: UnvalidatedBookData):
        if len(data.title) < 3:
            raise Exception('Title should be bigger than 3 chars')

        self.title = data.title
        self.author_data = data.author_data


class ExistingFile:
    def __init__(self, location: str):
        if not os.path.exists(location):
            raise Exception("File does not exist")

        self.location = location

class IntBiggerThanZero:
    def __init__(self, value: int):
        if value < 1:
            raise Exception("Must be bigger than zero")

        self.value = value


LinesToLoadLimit = IntBiggerThanZero

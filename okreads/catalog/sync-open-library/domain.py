from typing import NamedTuple, Any, Callable, List, NewType, Generator
from okreads.domain import ExistingFile
# public interface
# @todo create command generic type


SyncOpenLibraryCmd = NamedTuple('SyncOpenLibraryCmd', [('filename', str)])
BookPersistedEvent = NamedTuple('BookPersistedEvent', [('persisted_book_data', 'PersistedBookData')])

BookPersistedEvents = Generator[BookPersistedEvent, None, None]
WorkflowInterface = Callable[[SyncOpenLibraryCmd], BookPersistedEvents]

# private interface

OpenLibraryBookReference = NewType('OpenLibraryBookReference', str)
LinesToLoadLimit = NewType('LinesToLoadLimit', int)
BookReferences = Generator[OpenLibraryBookReference, None, None]

LoadOpenLibraryBookReference = Callable[[ExistingFile, LinesToLoadLimit], BookReferences]

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


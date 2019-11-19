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

ValidatedBookData = NewType('ValidatedBookData', UnvalidatedBookData)

ValidateBook = Callable[[UnvalidatedBookData], ValidatedBookData]
PersistedBookData = NewType('PersistedBookData', ValidatedBookData)

PersistBook = Callable[[ValidatedBookData], PersistedBookData]


def validate_book_data(unvalidated: UnvalidatedBookData) -> ValidatedBookData:
    return ValidatedBookData(unvalidated)

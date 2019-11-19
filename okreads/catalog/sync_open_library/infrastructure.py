from typing import Optional
from .domain import LinesToLoadLimit, BookReferences, OpenLibraryBookReference, OpenLibraryBookReference, UnvalidatedBookData, PersistedBookData, ValidatedBookData, ExistingFile
# from tqdm import tqdm
# import pandas as pd

def open_library_loader_concrete(file: ExistingFile, limit: Optional[LinesToLoadLimit]) -> BookReferences:
    # limit = limit if limit is None else int(limit)
    # data = pd.read_csv(file.location, delimiter='   ', header=None)
    # for i, entity in tqdm(enumerate(data[4].tolist())):
    #     if limit and i >= limit:
    #         break

    yield OpenLibraryBookReference('foo')


def book_data_loader_concrete(referece: OpenLibraryBookReference) -> UnvalidatedBookData:
    return UnvalidatedBookData(author_data=None, title='foo')


def persist_book(validated: ValidatedBookData)-> PersistedBookData:
    return PersistedBookData(validated)



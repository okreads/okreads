from okreads.domain import ExistingFile

from domain import LoadOpenLibraryBookReference, BookPersistedEvents, SyncOpenLibraryCmd, BookPersistedEvent, LinesToLoadLimit, PersistedBookData, ValidatedBookData, UnvalidatedBookData, LoadOpenLibraryBookData, PersistBook

from infrastructure import open_library_loader_concrete, book_data_loader_concrete, persist_book

def factory() -> 'Workflow':
    return Workflow(open_library_loader_concrete, book_data_loader_concrete, persist_book)



class Workflow:
    def __init__(self, book_reference_loader: LoadOpenLibraryBookReference, book_data_loader: LoadOpenLibraryBookData, persist_book: PersistBook):
        self.book_reference_loader = book_reference_loader
        self.book_data_loader = book_data_loader
        self.persist_book = persist_book

    def run(self, cmd: SyncOpenLibraryCmd) -> BookPersistedEvents:
        for reference in self.book_reference_loader(ExistingFile(cmd.filename), LinesToLoadLimit(1)):
            unvalidated_book_data = self.book_data_loader(reference)
            validated_book_data = ValidatedBookData(unvalidated_book_data)
            persisted_book = persist_book(validated_book_data)
            yield BookPersistedEvent(persisted_book_data=persisted_book)


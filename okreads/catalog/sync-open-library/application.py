from okreads.domain import ExistingFile

from domain import LoadOpenLibraryBookReference, BookPersistedEvents, SyncOpenLibraryCmd, BookPersistedEvent, LinesToLoadLimit, PersistedBookData, ValidatedBookData, UnvalidatedBookData, LoadOpenLibraryBookData

from infrastructure import open_library_loader_concrete, book_data_loader_concrete


class Workflow:
    @staticmethod
    def factory() -> 'Workflow':
        return Workflow(open_library_loader_concrete, book_data_loader_concrete)

    def __init__(self, book_reference_loader: LoadOpenLibraryBookReference, book_data_loader: LoadOpenLibraryBookData):
        self.book_reference_loader = book_reference_loader
        self.book_data_loader = book_data_loader

    def run(self, cmd: SyncOpenLibraryCmd) -> BookPersistedEvents:

        for reference in self.book_reference_loader(ExistingFile(cmd.filename), LinesToLoadLimit(1)):
            unvalidated_book_data = self.book_data_loader(reference)
            validated_book_data = ValidatedBookData(unvalidated_book_data)
            yield BookPersistedEvent(persisted_book_data=PersistedBookData(validated_book_data))

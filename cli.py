import click
import pandas as pd
from okreads.book import Book
import json


@click.command()
@click.option('--dumpfile', help='the file dump path to import')
@click.option('--limit', default=None, help="pass a limit if you want to import just some files")
def import_open_library(dumpfile, limit):

    limit = limit if limit is None else int(limit)
    data = pd.read_csv(dumpfile, delimiter='	', header=None)

    for i, entity in enumerate(data[4].tolist()):
        if limit and i >= limit:
            break

        book = Book.from_dict(json.loads(entity))
        print(book.to_dict())


if __name__ == '__main__':
    import_open_library()

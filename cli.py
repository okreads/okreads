import click
import pandas as pd
from okreads.book import Book
import json
import psycopg2

from okreads.db import Db


@click.group()
def cli():
    pass


@cli.command()
@click.option('--dumpfile',
              default='data_samples/open_library_1000',
              help='the file dump path to import')
@click.option('--limit', default=None, help="pass a limit if you want to import just some files")
def import_open_library(dumpfile, limit):

    limit = limit if limit is None else int(limit)
    data = pd.read_csv(dumpfile, delimiter='	', header=None)
    for i, entity in enumerate(data[4].tolist()):
        if limit and i >= limit:
            break

        book = Book.from_dict(json.loads(entity))

        Db.execute("INSERT INTO book (title, author) VALUES (%s, %s)", (book.title, book.author))


@cli.command()
def create_database():
    Db.execute(
        "CREATE TABLE public.book (id serial PRIMARY KEY, isbn char(255), title char(255), author char(255));"
    )


if __name__ == '__main__':
    cli()

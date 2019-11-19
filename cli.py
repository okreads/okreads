import click
import pandas as pd
from okreads.book import Book
import json
from tqdm import tqdm
from okreads.db import Db
from okreads.openlibrary import import_author, import_book


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
    for i, entity in tqdm(enumerate(data[4].tolist())):
        if limit and i >= limit:
            break

        import_book(entity)



if __name__ == '__main__':
    cli()

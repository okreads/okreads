import click
import pandas as pd


@click.command()
@click.option('--dumpfile', help='the file dump path to import')
@click.option('--limit', default=100, help="pass a limit if you want to import just some files")
def import_open_library(dumpfile, limit):
    data = pd.read_csv(dumpfile, sep='      ')
    data.head()


if __name__ == '__main__':
    import_open_library()

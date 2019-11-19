import click
from okreads.catalog.sync_open_library.domain import SyncOpenLibraryCmd

@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--dumpfile',
              default='data_samples/open_library_1000',
              help='the file dump path to import')
@click.option('--limit', default=None, help="pass a limit if you want to import just some files")
def import_open_library(dumpfile: str, limit: int) -> None:
    SyncOpenLibraryCmd(filename=dumpfile, limit=limit)


if __name__ == '__main__':
    cli()

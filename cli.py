import sys, os

sys.path.insert(0, os.path.abspath('.'))

import click

from source.utils.m4a_file_to_csv_converter import M4AFileToCSVConverter
from source.utils.data_explorer import DataExplorer


@click.group()
def cli():
    pass


@click.command(name='main')
def main():
    print("Nothing to run")


@click.command(name='sync_data')
@click.option('--force', '-f', is_flag=True, help="Will print verbose messages.")
def convert_all_data(force):
    for file_name in DataExplorer.get_m4a_file_paths():
        M4AFileToCSVConverter.convert(file_name, force_converting=force)


cli.add_command(main)
cli.add_command(convert_all_data)

if __name__ == "__main__":
    cli()

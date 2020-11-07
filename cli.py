import sys
import os

sys.path.insert(0, os.path.abspath('.'))

import click

from source.utils.m4a_file_to_csv_converter import M4AFileToCSVConverter
from source.utils.data_explorer import DataExplorer
from source.infographics.fourier_transform_plot import MultipleFourierTransformPlot
from source.ft.data_fourier_transformer import MultipleDataFourierTransformer


@click.group()
def cli():
    pass


@click.command(name='show_multiple_ft_plot')
def show_multiple_ft_plot():
    fourier_transforms = list()
    data_types = ['intact', 'damaged', 'slot']
    for data_type in data_types:
        fourier_transforms.append(MultipleDataFourierTransformer.get_fourier_transformed(data_type))
    MultipleFourierTransformPlot.plot_and_show_on_one_axis(fourier_transforms, data_types)


@click.command(name='sync_data')
@click.option('--force', '-f', is_flag=True, help="Will print verbose messages.")
def convert_all_data(force):
    for file_name in DataExplorer.get_m4a_file_paths():
        M4AFileToCSVConverter.convert(file_name, force_converting=force)


cli.add_command(show_multiple_ft_plot)
cli.add_command(convert_all_data)

if __name__ == "__main__":
    cli()

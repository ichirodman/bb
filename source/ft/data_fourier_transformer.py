from source.utils.data_csv_reader import DataCSVReader, DataExplorer

import numpy as np


class DataFourierTransformer:
    @staticmethod
    def transform(csv_reader: DataCSVReader):
        time, pressure = csv_reader.get_content()
        fourier_transform = np.fft.rfft(pressure, norm="ortho")
        return fourier_transform


class MultipleDataFourierTransformer:
    @staticmethod
    def get_fourier_transformed(data_type: str):
        fourier_transform = None
        for csv_file in DataExplorer.get_csv_files_paths(data_type):
            csv_reader = DataCSVReader(csv_file)
            ft_i = DataFourierTransformer().transform(csv_reader)
            if fourier_transform is None:
                fourier_transform = ft_i
            else:
                size = min(len(fourier_transform), len(ft_i))
                fourier_transform = fourier_transform[0:size] * ft_i[0:size]
        return fourier_transform

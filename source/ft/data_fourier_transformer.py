from source.utils.data_csv_reader import DataCSVReader

import numpy as np


class DataFourierTransformer:
    @staticmethod
    def transform(data_csv: DataCSVReader):
        time, pressure = data_csv.get_content()
        fourier_transform = np.fft.rfft(pressure, norm="ortho")
        return fourier_transform

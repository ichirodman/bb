from source.utils.data_csv_reader import DataCSVReader
from source.ft.data_fourier_transformer import DataFourierTransformer

from matplotlib import pyplot as plt
import numpy as np


class FourierTransformPlot:
    @staticmethod
    def plot_and_show(data_reader: DataCSVReader, fourier_range_len=None):
        fourier_transform = DataFourierTransformer.transform(data_reader)

        fourier_range = np.arange(len(fourier_transform))

        if fourier_range_len:
            fourier_range = np.arange(fourier_range_len) if \
                fourier_range_len <= len(fourier_transform) else np.arange(len(fourier_transform))

        print(len(fourier_range))

        fourier_transform = np.abs(fourier_transform)

        plt.plot(fourier_range, fourier_transform, 'r')
        plt.xlabel('Time')
        plt.xlabel('Frequencies')
        plt.grid()

        plt.show()
        plt.clf()

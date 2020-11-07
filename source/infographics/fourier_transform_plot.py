from matplotlib import pyplot as plt
import numpy as np


class FourierTransformPlot:
    @staticmethod
    def plot_and_show(fourier_transform):
        fourier_range = np.arange(len(fourier_transform))

        fourier_transform = np.abs(fourier_transform)

        plt.plot(fourier_range, fourier_transform, 'r')
        plt.xlabel('Time')
        plt.xlabel('Frequencies')
        plt.grid()

        plt.show()
        plt.clf()

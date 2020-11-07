from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler


class FourierTransformPlot:
    @staticmethod
    def plot_and_show(fourier_transform, data_type: str):
        fourier_range = np.arange(len(fourier_transform))
        fourier_transform = np.abs(fourier_transform)

        plt.plot(fourier_range, fourier_transform, 'r')
        plt.title('FFT of \'{}\' sample'.format(data_type))
        plt.xlabel('Time')
        plt.ylabel('Frequencies')
        plt.grid()
        plt.show()
        plt.clf()


class MultipleFourierTransformPlot:
    @staticmethod
    def plot_and_show_on_different_axes(fourier_transforms: list, data_types: list):
        if len(fourier_transforms) < 2:
            raise TooFewSequencesToPlot
        else:
            fourier_ranges = [np.arange(len(i)) for i in fourier_transforms]
            fourier_transforms = [np.abs(i) for i in fourier_transforms]

            fig, axes = plt.subplots(len(fourier_transforms))

            for i in range(len(fourier_transforms)):
                axes[i].plot(fourier_ranges[i], fourier_transforms[i], 'r')
                axes[i].set_title('FFT of \'{}\' sample'.format(data_types[i]))
                axes[i].set_xlabel('Time')
                axes[i].set_ylabel('Frequencies')
                axes[i].grid()

            plt.tight_layout()
            plt.show()
            plt.clf()

    @staticmethod
    def plot_and_show_on_one_axis(fourier_transforms: list, data_types: list):
        if len(fourier_transforms) < 2:
            raise TooFewSequencesToPlot
        else:
            fourier_ranges = [np.arange(len(i)) for i in fourier_transforms]
            fourier_transforms = [np.abs(i) for i in fourier_transforms]

            for i in range(len(fourier_transforms)):
                fourier_transforms[i] = StandardScaler().fit_transform(fourier_transforms[i].reshape(-1, 1))

            colors = ['r', 'g', 'b', 'y']

            for i in range(len(fourier_transforms)):
                plt.plot(fourier_ranges[i], fourier_transforms[i], colors[i])

            plt.title('FFT of {} samples'.format(', '.join(map(lambda x: "\'" + x + "\'", data_types))))
            plt.xlabel('Time')
            plt.ylabel('Frequencies')
            plt.legend(data_types)
            plt.grid()

            plt.tight_layout()
            plt.show()
            plt.clf()


class TooFewSequencesToPlot(Exception):
    pass

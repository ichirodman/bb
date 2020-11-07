import os
import pandas as pd
import plotly.express as px

RELATIVE_PATH_TO_SAMPLES_DIR = './data/csv/intact/'
RELATIVE_PATH_TO_OUTPUT_PLOTS_DIR = './infographics/output_plots/'


def ask_file_name():
    all_slice_matches_files = os.listdir(RELATIVE_PATH_TO_SAMPLES_DIR)
    print('Enter file number:')
    print('------------------')
    for i in range(len(all_slice_matches_files)):
        print('{} | {}'.format(i + 1, all_slice_matches_files[i]))
    print('------------------')
    try:
        file_index = int(input()) - 1
        if file_index < 0:
            raise IndexError
        return all_slice_matches_files[file_index]
    except ValueError:
        print('Wrong input format - value error')
        exit()
    except IndexError:
        print('File with this number does not exist - index error')
        exit()


def get_path(file_name):
    return RELATIVE_PATH_TO_SAMPLES_DIR + file_name


def make_plot(file_name):
    file_path = get_path(file_name)
    df = pd.read_csv(file_path)
    fig = px.line(df, x='Unnamed: 0', y='0', title='Sound')
    fig.show()


if __name__ == "__main__":
    needed_file_name = ask_file_name()
    make_plot(needed_file_name)

import csv
import numpy as np

from source.utils.data_explorer import DataExplorer


class DataCSVReader:
    _content: list = None

    def __init__(self, filename: str):
        csv_path = DataExplorer.get_path_for_name(filename)
        with open(csv_path, 'r') as csv_file:
            self._content = DataCSVReader._read_csv(csv_file)

    @staticmethod
    def _read_csv(file_obj) -> list:
        reader = csv.reader(file_obj)
        row_data = [row for row in reader]
        time = np.int64([row[0] for row in row_data[1:]])
        pressure = np.real([row[1] for row in row_data])
        return [time, pressure]

    def get_content(self):
        return self._content

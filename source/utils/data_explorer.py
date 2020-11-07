from pathlib import Path

from source.settings.project_paths import *

import os


class DataExplorer:
    @staticmethod
    def get_m4a_file_paths():
        return DataExplorer.get_m4a_files_paths('damaged/') + DataExplorer.get_m4a_files_paths('intact/')

    @staticmethod
    def get_m4a_files_paths(dir_type: str):
        directory_path = M4A_SAMPLES_DIR_PATH.format(dir_type)
        return [dir_type + '/' + i for i in os.listdir(directory_path) if i.split('.')[-1] == 'm4a']

    @staticmethod
    def file_exist(filename: str) -> bool:
        path = DataExplorer.get_path_for_name(filename)
        return Path(path).exists()

    @staticmethod
    def get_path_for_name(filename: str) -> str:
        extension = DataExplorer.get_extension(filename)
        return DataExplorer.get_path_for_extension(extension).format(filename)

    @staticmethod
    def get_path_for_extension(extension: str) -> str:
        if extension == 'csv':
            return CSV_SAMPLES_DIR_PATH
        elif extension == 'wav':
            return WAV_SAMPLES_FIR_PATH
        elif extension == 'm4a':
            return M4A_SAMPLES_DIR_PATH
        else:
            raise UnknownFileFormat

    @staticmethod
    def get_extension(filename: str) -> str:
        return filename.split('.')[-1]


class UnknownFileFormat(Exception):
    pass

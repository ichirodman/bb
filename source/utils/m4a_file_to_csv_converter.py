from pydub import AudioSegment
from scipy.io import wavfile
import pandas as pd

from source.utils.data_explorer import DataExplorer


class M4AFileToCSVConverter:
    @staticmethod
    def convert(m4a_name: str, force_converting=False) -> None:
        wav_name = M4AFileToCSVConverter._replace_extension(m4a_name, 'wav')
        csv_name = M4AFileToCSVConverter._replace_extension(m4a_name, 'csv')
        if not DataExplorer.file_exist(wav_name) or force_converting:
            M4AFileToCSVConverter._convert_m4a_to_wav(m4a_name)
        if not DataExplorer.file_exist(csv_name) or force_converting:
            M4AFileToCSVConverter._convert_wav_to_csv(wav_name)

    @staticmethod
    def _convert_m4a_to_wav(m4a_name: str) -> None:
        audio_segment = M4AFileToCSVConverter._get_audio_segment(m4a_name)
        wav_name = M4AFileToCSVConverter._replace_extension(m4a_name, 'wav')
        wav_path = DataExplorer.get_path_for_extension('wav').format(wav_name)
        audio_segment.export(wav_path, format='wav')

    @staticmethod
    def _convert_wav_to_csv(wav_name: str) -> None:
        wav_path = DataExplorer.get_path_for_extension('wav').format(wav_name)
        _, data = wavfile.read(wav_path)
        wav_data = pd.DataFrame(data)
        csv_name = M4AFileToCSVConverter._replace_extension(wav_name, 'csv')
        csv_path = DataExplorer.get_path_for_extension('csv').format(csv_name)
        wav_data.to_csv(csv_path, mode='w')

    @staticmethod
    def _get_audio_segment(name: str) -> AudioSegment:
        extension = DataExplorer.get_extension(name)
        path = DataExplorer.get_path_for_extension(extension).format(name)
        audio_segment = AudioSegment.from_file(path, extension)
        return audio_segment

    @staticmethod
    def _replace_extension(name: str, extension_replace_to: str) -> str:
        return '.'.join(name.split('.')[:-1] + [extension_replace_to])

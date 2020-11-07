import pyaudio
from scipy.io import wavfile
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

time_of_recording = 3
wave_file_name = "./data/damaged/file_note.wav"
csv_path = "output_mono_file_note.csv"


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    row_data = [row for row in reader]
    temp = np.int64([row[0] for row in row_data[1:]])
    time = temp * time_of_recording / temp[-1]
    pressure = np.real([row[1] for row in row_data])
    return time, pressure


def find_device():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)['name'])


def record_sound():
    import wave
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * time_of_recording)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_csv():
    samrate, data = wavfile.read(str(wave_file_name))
    wavData = pd.DataFrame(data)
    # wavData.columns = ['M']
    wavData.to_csv(str(csv_path), mode='w')


record_sound()
get_csv()

with open(csv_path, "r") as f_obj:
    time, pressure = csv_reader(f_obj)  # Generate frequencies
    print(time)
    signal_length = len(pressure)
    frequencies = np.arange(signal_length) / time_of_recording
    frequencies = frequencies[range(signal_length // 2 + 1)]

    fourier_transform = np.fft.rfft(pressure, norm="ortho")
    second_fourier_transform = np.fft.rfft(pressure, norm="ortho")

    fig, ax = plt.subplots(2)
    ax[0].plot(frequencies[0:20000], np.abs(fourier_transform)[0:20000], 'r')
    ax[0].set_xlabel('Frequency')
    ax[0].set_ylabel('Pressure')

    ax[1].plot(frequencies[0:1000], np.abs(second_fourier_transform)[0:1000], 'r')
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('Amplitude')

    # fig.tight_layout()
    plt.show()

# from moviepy.editor import *

# # Mengubah file MP4 menjadi file audio WAV
# def mp4_to_wav(mp4_path, wav_path):
#     video = VideoFileClip(mp4_path)
#     audio = video.audio
#     audio.write_audiofile(wav_path)

# # Contoh penggunaan fungsi mp4_to_wav
# mp4_path = "psd cover.mp4"
# wav_path = "psd cover 2.wav"
# mp4_to_wav(mp4_path, wav_path)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

# Baca file audio
fs, audio = wavfile.read('psd cover 2.wav')

# Ambil satu saluran audio (jika audio stereo)
audio = audio[:, 0]

# Konfigurasi spektrogram
nperseg = 1024  # Jumlah sampel per segmen
noverlap = 512  # Jumlah sampel tumpang tindih antara segmen
window = 'hann'  # Jenis window yang digunakan

# Hitung spektrogram
frequencies, times, S = spectrogram(audio, fs=fs, nperseg=nperseg, noverlap=noverlap, window=window)

# Plot spektrogram
plt.figure(figsize=(10, 6))
plt.pcolormesh(times, frequencies, 10 * np.log10(S), shading='auto', cmap='jet')
plt.colorbar(label='Power Spectral Density (dB/Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram')
plt.show()

# import numpy as np
# from pydub import AudioSegment

# # Mendapatkan spektrum frekuensi dari suatu audio segment
# def get_frequency_spectrum(segment):
#     # Mendapatkan array dari sampel audio
#     samples = segment.get_array_of_samples()
#     # Menghitung transformasi Fourier cepat (FFT) pada array sampel audio
#     fft = np.fft.fft(samples)
#     # Menghitung magnitudo spektrum frekuensi
#     magnitude = 20 * np.log10(np.abs(fft) / 32768)
#     # Mengembalikan spektrum frekuensi
#     return magnitude

# # Menentukan frekuensi yang perlu ditingkatkan untuk meningkatkan kejelasan vokal
# def determine_vocal_clarity(audio_path):
#     # Memuat file audio sebagai AudioSegment
#     audio = AudioSegment.from_file(audio_path)
#     # Mendapatkan spektrum frekuensi dari file audio
#     frequency_spectrum = get_frequency_spectrum(audio)
#     # Mendapatkan frekuensi yang memiliki magnitudo tertinggi
#     max_magnitude_index = np.argmax(frequency_spectrum)
#     max_magnitude_freq = max_magnitude_index * (audio.frame_rate / len(frequency_spectrum))
#     # Mengembalikan frekuensi yang perlu ditingkatkan
#     return max_magnitude_freq

# # Contoh penggunaan fungsi determine_vocal_clarity
# audio_path = "psd cover 2.wav"
# vocal_clarity_frequency = determine_vocal_clarity(audio_path)
# print("Frekuensi yang perlu ditingkatkan untuk meningkatkan kejelasan vokal:", vocal_clarity_frequency)

# import numpy as np
# import pydub

# # Membaca file WAV
# file_path = "psd cover 2.wav"
# audio_data = pydub.AudioSegment.from_wav(file_path)

# # Mendefinisikan jumlah band dan frekuensi pusat masing-masing band
# num_bands = 5
# center_frequencies = np.array([125, 500, 1000, 2000, 8000])

# # Menentukan lebar pita masing-masing band
# bandwidths = np.zeros(num_bands)
# for i in range(num_bands):
#     if i == 0:
#         bandwidths[i] = center_frequencies[i] / 2
#     elif i == num_bands - 1:
#         bandwidths[i] = audio_data.frame_rate / 2 - center_frequencies[i - 1]
#     else:
#         bandwidths[i] = (center_frequencies[i] - center_frequencies[i - 1]) / 2

# # Menentukan faktor Q dari lebar pita
# q_factors = np.divide(center_frequencies, bandwidths)

# # Menentukan jumlah filter IIR untuk setiap band equalizer
# num_filters = np.ones(num_bands, dtype=int)
# num_filters[1:-1] = 2

# # Menentukan jumlah koefisien filter IIR untuk setiap band equalizer
# num_taps = np.ones(num_bands, dtype=int) * 101
# num_taps[0] = 51
# num_taps[-1] = 51

# # Output hasil
# print("Faktor Q untuk setiap band equalizer:", q_factors)
# print("Jumlah filter IIR untuk setiap band equalizer:", num_filters)
# print("Jumlah koefisien filter IIR untuk setiap band equalizer:", num_taps)


import numpy as np
import pydub
from scipy import signal

# # Membaca file WAV
# file_path = "psd cover 2.wav"
# audio_data = pydub.AudioSegment.from_wav(file_path)
# sample_rate = audio_data.frame_rate

# # Mendefinisikan jumlah band dan frekuensi pusat masing-masing band
# num_bands = 5
# center_frequencies = np.array([125, 500, 1000, 2000, 8000])

# # Menentukan lebar pita masing-masing band
# bandwidths = np.zeros(num_bands)
# for i in range(num_bands):
#     if i == 0:
#         bandwidths[i] = center_frequencies[i] / 2
#     elif i == num_bands - 1:
#         bandwidths[i] = sample_rate / 2 - center_frequencies[i - 1]
#     else:
#         bandwidths[i] = (center_frequencies[i] - center_frequencies[i - 1]) / 2

# # Menentukan faktor Q dari lebar pita
# q_factors = np.divide(center_frequencies, bandwidths)

# # Merancang filter setiap band equalizer
# b_coeffs = []
# a_coeffs = []
# for i in range(num_bands):
#     if i == 0:
#         # High-pass filter
#         b, a = signal.butter(4, center_frequencies[i] / (sample_rate / 2), btype="highpass")
#     elif i == num_bands - 1:
#         # Low-pass filter
#         b, a = signal.butter(4, center_frequencies[i] / (sample_rate / 2), btype="lowpass")
#     else:
#         # Band-pass filter
#         b, a = signal.butter(4, [center_frequencies[i-1] / (sample_rate / 2), center_frequencies[i] / (sample_rate / 2)], btype="bandpass")
#     b_coeffs.append(b)
#     a_coeffs.append(a)

# Output hasil
# for i in range(num_bands):
#     print("Band", i+1)
#     print("B koefisien:", b_coeffs[i])
#     print("A koefisien:", a_coeffs[i])

import pydub

# Membaca file WAV
file_path = "psd cover 2.wav"
audio_data = pydub.AudioSegment.from_wav(file_path)

# Menyesuaikan kekuatan audio dengan gain 10 dB
adjusted_audio_data = audio_data.apply_gain(207)

# Menyimpan file WAV yang telah disesuaikan kekuatannya
output_file_path = "cover tingkat suara 2.wav"
adjusted_audio_data.export(output_file_path, format="wav")

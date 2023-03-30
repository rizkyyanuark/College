import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.io.wavfile import write
from scipy.io import wavfile

# -----mengubah file Data sinyal csv menjadi wav-----
# Membaca file CSV
with open('Data_sinyal.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Menentukan parameter WAV (contoh: frekuensi sampling 44100 Hz)
fs = 48000

# Menyimpan data sinyal dalam format WAV
write('UTS_Sinyal.wav', fs, data_np)
# ----------------------------------------


# ---membuat plot atau sinyal dari hasil sinyal.wav---

# Membaca file WAV
fs, data = wavfile.read('UTS_sinyal.wav')

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Melakukan transformasi FFT
fft = np.fft.fft(data_np)

# Menampilkan hasil transformasi FFT
print(fft)

# Membaca file WAV
fs, data = wavfile.read('UTS_sinyal.wav')

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Melakukan transformasi FFT
fft = np.fft.fft(data_np)

# Menentukan skala frekuensi
freq = np.fft.fftfreq(data_np.shape[-1], d=1/fs)

# Membuat plot sinyal input
plt.subplot(2, 1, 1)
plt.plot(data_np)
plt.title('Sinyal Input')
plt.xlabel('Waktu')
plt.ylabel('Amplitudo')

# Membuat plot frekuensi hasil transformasi FFT
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fft))
plt.title('Frekuensi Hasil Transformasi FFT')
plt.xlabel('Frekuensi')
plt.ylabel('Amplitudo')

# Menampilkan plot
plt.show()

# ---------------------------------------


# -----mengubah file Data noise csv menjadi wav-----

# Membaca file CSV
with open('Data_noise.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Menentukan parameter WAV (contoh: frekuensi sampling 44100 Hz)
fs = 48000

# Menyimpan data sinyal dalam format WAV
write('UTS_noise.wav', fs, data_np)

# ---membuat plot atau sinyal dari hasil sinyal.wav---

# Membaca file WAV
fs, data = wavfile.read('UTS_noise.wav')

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Melakukan transformasi FFT
fft = np.fft.fft(data_np)

# Menampilkan hasil transformasi FFT
print(fft)

# -----------------------------------------------------


# -----penggabungan sinyal dan nosie------
# Baca file UTS_sinyal.wav
rate, signal = wavfile.read('UTS_Sinyal.wav')

# Baca file Data_noise.csv
noise_data = np.genfromtxt('Data_noise.csv', delimiter=',')

# Pastikan ukuran data noise sama dengan ukuran data sinyal
assert len(noise_data) == len(signal)

# Gabungkan data noise ke data sinyal
signal_with_noise = signal.astype(float) + noise_data

# Simpan data sinyal dengan noise ke file baru
wavfile.write('UTS_Sinyal_with_noise.wav', rate,
              signal_with_noise.astype(np.int16))

# --------------------------------------------------------------


# ------plot frekuensi hasil transformasi FFT--------
# Membaca file WAV
fs, data = wavfile.read('UTS_Sinyal_dengan_noise.wav')

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Melakukan transformasi FFT
fft = np.fft.fft(data_np)

# Menampilkan hasil transformasi FFT
print(fft)

# Membaca file WAV
fs, data = wavfile.read('UTS_Sinyal_dengan_noise.wav')

# Mengubah data ke dalam format array numpy
data_np = np.array(data, dtype=float)

# Melakukan transformasi FFT
fft = np.fft.fft(data_np)

# Menentukan skala frekuensi
freq = np.fft.fftfreq(data_np.shape[-1], d=1/fs)

# Membuat plot sinyal input
plt.subplot(2, 1, 1)
plt.plot(data_np)
plt.title('Sinyal Input')
plt.xlabel('Waktu')
plt.ylabel('Amplitudo')

# Membuat plot frekuensi hasil transformasi FFT
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fft))
plt.title('Frekuensi Hasil Transformasi FFT')
plt.xlabel('Frekuensi')
plt.ylabel('Amplitudo')

# Menampilkan plot
plt.show()

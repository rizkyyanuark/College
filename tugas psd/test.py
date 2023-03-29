from scipy.io.wavfile import write
# import numpy as np
# import matplotlib.pyplot as plt
# data = np.genfromtxt('Data_sinyal.csv', delimiter=',')
# data = np.int16(data / np.max(np.abs(data)) * 32767)
# write('Data_siyal_csv_yg_diubah.wav', 48000, data)
# fft_data = np.fft.fft(data)
# plt.plot(np.abs(fft_data))
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Baca data sinyal dari file .csv
data = np.genfromtxt('Data_sinyal.csv', delimiter=',')

# Normalisasi data menjadi bilangan bulat 16-bit
data = np.int16(data / np.max(np.abs(data)) * 32767)

# Baca data noise dari file .csv
noise = np.genfromtxt('Data_noise.csv', delimiter=',')

# Normalisasi data noise menjadi bilangan bulat 16-bit
noise = np.int16(noise / np.max(np.abs(noise)) * 32767)

# Tambahkan noise pada data sinyal
data_with_noise = np.int16(data + noise)

# Transformasi FFT
fft_data = np.fft.fft(data_with_noise)

# Hitung amplitudo spektrum frekuensi
amplitude_spectrum = np.abs(fft_data)

# # Hitung skala frekuensi dalam Hz
freq_scale = np.fft.fftfreq(len(data_with_noise), d=1/44100)

# Plot sinyal input dengan noise
time_scale = np.linspace(0, len(data_with_noise)/44100, len(data_with_noise))
plt.subplot(2, 1, 1)
plt.plot(time_scale, data_with_noise)
plt.xlabel('Waktu (detik)')
plt.ylabel('Amplitudo')

# Plot spektrum frekuensi
plt.subplot(2, 1, 2)
plt.plot(freq_scale[:len(data_with_noise)//2],
         amplitude_spectrum[:len(data_with_noise)//2])
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Amplitudo')
write('Data_siyal_csv_yg_diubah.wav', 48000, data)
plt.show()

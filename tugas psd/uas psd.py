import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy.fft import fft, fftfreq
import librosa
from scipy.signal import spectrogram

# FFT
data, sr = librosa.load('UTS_Sinyal_with_noise.wav')

def FFT(file, judul):
    X = fft(file)
    X_mag = np.absolute(X)
    f = np.linspace(0, sr, len(X_mag))
    plt.figure(figsize=(13, 5))
    plt.plot(f[:len(f)//2], X_mag[:len(f)//2])
    plt.xlabel("frekuensi (Hz)")
    plt.ylabel('Amplitudo')
    plt.title(judul)


# Load the WAV file
try:
    sampling_rate, data = wavfile.read('UTS_Sinyal_with_noise.wav')
except FileNotFoundError:
    print("File not found.")
    exit()
except Exception as e:
    print("An error occurred while reading the file:", e)
    exit()

# Compute and plot the FFT of the audio data
FFT(data, 'FFT of Audio Data')

# Display the plot
plt.show()

#Bandpass Filter
# Memuat File wav
try:
    sampling_rate, data = wavfile.read('UTS_Sinyal_with_noise.wav')
except FileNotFoundError:
    print("File not found.")
    exit()
except Exception as e:
    print("An error occurred while reading the file:", e)
    exit()

#menentukan lowcut dan highcut
cutoff_low = 100 # Lower cutoff frequency (in Hz)
cutoff_high = 3500  # Upper cutoff frequency (in Hz)
order = 4  # Filter order

b, a = signal.butter(order, [cutoff_low, cutoff_high], fs=sampling_rate, btype='band')
filtered_data = signal.lfilter(b, a, data)

# VVisualisasi suara original
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(data)
plt.title('Original Sound')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Visualisasi suara filter
plt.subplot(1, 2, 2)
plt.plot(filtered_data)
plt.title('Filtered Sound')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Menyimpan hasil filter ke file wav baru
wavfile.write('sinyal uts1.wav', sampling_rate, filtered_data.astype(np.int16))

# Display the plots
plt.tight_layout()
plt.show()



#Spectrogram
# Membaca file audio
sample_rate, data = wavfile.read('UTS_Sinyal_with_noise.wav')

# Menghitung spektrogram
frequencies, times, spectrogram_data = spectrogram(data, fs=sample_rate)

# Menampilkan spektrogram
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Power Spectral Density [dB]')
plt.title('Spectrogram Before Filtering')
plt.show()

# Membaca file audio
sample_rate, data = wavfile.read('sinyal uts1.wav')

# Menghitung spektrogram
frequencies, times, spectrogram_data = spectrogram(data, fs=sample_rate)

# Menampilkan spektrogram
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Power Spectral Density [dB]')
plt.title('Spectrogram After Filtering')
plt.show()

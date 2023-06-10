import pydub
from scipy import signal
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.fft import fft
import numpy as np
import librosa
import scipy
data, sr = librosa.load('output2.wav')


def FFT(file, judul):
    X = fft(file)
    X_mag = np.absolute(X)
    f = np.linspace(0, sr, len(X_mag))
    plt.figure(figsize=(13, 5))
    plt.plot(f[:len(f)//2], X_mag[:len(f)//2])
    plt.xlabel("frekuensi (Hz)")
    plt.title(judul)


# Load the WAV file
try:
    sampling_rate, data = wavfile.read('psd cover 2.wav')
except FileNotFoundError:
    print("File not found.")
    exit()
except Exception as e:
    print("An error occurred while reading the file:", e)
    exit()

# Compute and plot the FFT of the audio data
FFT(data, 'FFT of Audio Data')

# Display the plot
plt.show()


# Fungsi untuk menerapkan filter bandpass pada sinyal suara

def apply_bandpass_filter(data, sample_rate, lowcut, highcut):
    # Menentukan parameter filter
    order = 4  # Orde filter, angka bulat yang lebih besar dari 0
    nyquist = 0.5 * sample_rate
    low = lowcut / nyquist
    high = highcut / nyquist

    # Membuat filter bandpass
    b, a = signal.butter(order, [low, high], btype='band')

    # Menerapkan filter ke sinyal suara
    filtered_data = signal.lfilter(b, a, data)
    return filtered_data


# Membaca file audio
file_path = 'output2.wav'  # Ganti dengan path file audio Anda
sample_rate, data = wav.read(file_path)

# Menentukan frekuensi cutoff
lowcut = 1000  # Frekuensi cutoff bawah, dalam Hz
highcut = 5000  # Frekuensi cutoff atas, dalam Hz

# Menerapkan filter bandpass pada sinyal audio
filtered_data = apply_bandpass_filter(data, sample_rate, lowcut, highcut)

# Menyimpan hasil filter ke file audio
# Ganti dengan path file audio hasil filter
filtered_file_path = 'filtered audio.wav'
wav.write(filtered_file_path, sample_rate, filtered_data.astype(np.int16))


# Load the WAV file
try:
    sampling_rate, data = wavfile.read('filtered audio.wav')
except FileNotFoundError:
    print("File not found.")
    exit()
except Exception as e:
    print("An error occurred while reading the file:", e)
    exit()

# Apply the inverse filter
# Here, we'll use a Butterworth highpass filter
cutoff_frequency = 4000  # Cutoff frequency (in Hz)
order = 2  # Filter order

b, a = signal.butter(order, cutoff_frequency, fs=sampling_rate, btype='high')
filtered_data = signal.lfilter(b, a, data)

# Visualize the original sound
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(data)
plt.title('Original Sound')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Visualize the filtered sound
plt.subplot(1, 2, 2)
plt.plot(filtered_data)
plt.title('Filtered Sound')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Save the filtered sound to a new WAV file
wavfile.write('filtered.wav', sampling_rate, filtered_data.astype(np.int16))

# Display the plots
plt.tight_layout()
plt.show()


# Membaca file WAV
file_path = "filtered.wav"
audio_data = pydub.AudioSegment.from_wav(file_path)

# Menyesuaikan kekuatan audio dengan gain 10 dB
adjusted_audio_data = audio_data.apply_gain(10)

# Menyimpan file WAV yang telah disesuaikan kekuatannya
output_file_path = "cover tingkat suara 2.wav"
adjusted_audio_data.export(output_file_path, format="wav")

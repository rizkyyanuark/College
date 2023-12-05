import azure.cognitiveservices.speech as speechsdk
import tkinter as tk
from tkinter import messagebox, PhotoImage
import re


def recognize_speech():
    # Setel kunci dan wilayah dari sumber daya Azure Speech Anda
    speech_key = "5544cd8ec2fb442c8527470731b0daae"
    region = "southeastasia"

    # Buat objek konfigurasi dengan kunci dan wilayah
    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=region)

    # Atur bahasa pengenalan ke Bahasa Indonesia
    speech_config.speech_recognition_language = "id-ID"

    # Buat pengenal ucapan dengan konfigurasi
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    # Mulai pengenalan ucapan
    print("Mulai berbicara...")
    result = speech_recognizer.recognize_once()

    # Cetak hasil pengenalan ucapan
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        messagebox.showinfo("Hasil", "Terdeteksi: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        messagebox.showinfo("Hasil", "Tidak ada ucapan yang terdeteksi.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        messagebox.showerror("Error", "Pengenalan ucapan dibatalkan: {}".format(
            cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            messagebox.showerror("Error", "Kesalahan: {}".format(
                cancellation_details.error_details))


# Membuat window utama
root = tk.Tk()
root.title("Azure Speech Recognition")

# Menambahkan ikon aplikasi (ganti 'path_to_icon.ico' dengan path ikon yang sesuai)
root.iconbitmap(
    r'C:\Users\rizky\OneDrive\Dokumen\GitHub\test\testpython\project gui\profile.png')

# Menambahkan gambar latar belakang (ganti 'path_to_background_image.png' dengan path gambar yang sesuai)
background_image = PhotoImage(
    file=r'C:\Users\rizky\OneDrive\Dokumen\GitHub\test\testpython\project gui\profile.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Menambahkan label judul
title_label = tk.Label(root, text="say something",
                       font=("Helvetica", 24), bg="#ffffff")
title_label.pack(pady=(20, 10))

# Membuat tombol dengan styling
start_button = tk.Button(root, text="Mulai Pengenalan Ucapan", command=recognize_speech, font=(
    "Helvetica", 16), bg="#34A2FE", fg="#ffffff")
start_button.pack(pady=20)

# Menjalankan aplikasi GUI
root.mainloop()

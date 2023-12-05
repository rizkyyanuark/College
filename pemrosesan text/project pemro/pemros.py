import azure.cognitiveservices.speech as speechsdk
import tkinter as tk
from tkinter import messagebox, Text
from PIL import Image, ImageTk

# Fungsi untuk menghapus teks dari kotak teks
def clear_text():
    text_box.delete("1.0", tk.END)

# Fungsi pengenalan ucapan
def recognize_speech():
    # Setel kunci dan wilayah dari sumber daya Azure Speech Anda
    speech_key = "5544cd8ec2fb442c8527470731b0daae"
    region = "southeastasia"

    # Buat objek konfigurasi dengan kunci dan wilayah
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)

    # Atur bahasa pengenalan ke Bahasa Indonesia
    speech_config.speech_recognition_language = "id-ID"

    # Buat pengenal ucapan dengan konfigurasi
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    # Mulai pengenalan ucapan
    print("Mulai berbicara...")
    result = speech_recognizer.recognize_once()

    # Cetak hasil pengenalan ucapan
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text_box.insert(tk.END, result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        messagebox.showinfo("Hasil", "Tidak ada ucapan yang terdeteksi.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        messagebox.showerror("Error", "Pengenalan ucapan dibatalkan: {}".format(
            cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            messagebox.showerror("Error", "Kesalahan: {}".format(
                cancellation_details.error_details))

# Fungsi untuk analisis sentimen
def analyze_sentiment():
    # Ambil teks dari kotak teks
    text_to_analyze = text_box.get("1.0", tk.END)
    
    # Placeholder: Panggil layanan analisis sentimen di sini
    # Contoh: hasil = sentiment_analysis_service.analyze(text_to_analyze)
    # Untuk demo, kita akan menampilkan messagebox
    messagebox.showinfo("Analisis Sentimen", "Analisis sentimen akan dilakukan pada teks: " + text_to_analyze)

# Membuat window utama
root = tk.Tk()
root.title("Azure Speech Recognition")
root.geometry("1440x720")
root.resizable(0, 0)
root.state('zoomed')

# Menambahkan latar belakang gambar tanpa zoom
background_image = Image.open("page1.png")
background_resize = background_image.resize((1440, 720))
background_image = ImageTk.PhotoImage(background_resize)  # Ganti dengan path gambar Anda
background_label = tk.Label(root, image=background_image)
background_label.place(x = -2, y = -2)


# Menambahkan kotak teks
text_box = Text(root, height=12, width=55, bg="white", borderwidth = 0, font=('Constantia',12))
text_box.place(x = 200, y = 130)

# Membuat tombol untuk menghapus
image_trash= 'trash.png'  # Replace with the path to your image file
image_trash = Image.open(image_trash)
mic_resize = image_trash.resize((50,50))
image_trash = ImageTk.PhotoImage(mic_resize)  # Ganti dengan path gambar Anda
clear_button = tk.Button(root, command=clear_text, image=image_trash, width=50, height=50, borderwidth = 0, highlightthickness=0)
clear_button.place(x=830, y=230)

# Membuat tombol untuk pengenalan ucapan
image_mic = 'mic.png'  # Replace with the path to your image file
image_mic = Image.open(image_mic)
mic_resize = image_mic.resize((50,50))
image_mic = ImageTk.PhotoImage(mic_resize)
start_button = tk.Button(root, command=recognize_speech, image=image_mic, width=50, height=50, borderwidth = 0, highlightthickness=0)
start_button.place(x=830, y=170)

# Membuat tombol untuk analisis sentimen
sentiment_button = tk.Button(root, text="Analisis Sentimen", command=analyze_sentiment, font=("Helvetica", 16), bg="#545454", fg="white", borderwidth = 0)
sentiment_button.place(x=830, y=290)

# Menjalankan aplikasi GUI
root.mainloop()

import tkinter as tk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def update_chart():
    # hapus chart lama
    ax2.clear()
    # buat chart baru dengan data terbaru
    df = pd.read_excel('data.xlsx')
    gender_counts = df['Jenis Kelamin'].value_counts()
    labels = gender_counts.index
    sizes = gender_counts.values
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%',
            startangle=90)
    # refresh tampilan chart
    canvas.draw()


df = pd.read_excel('data.xlsx')
gender_counts = df['Jenis Kelamin'].value_counts()
plt.style.use('default')
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=['#9CA777', '#64C2A6', '#AADEA7'])

fig2, ax2 = plt.subplots()
ax2.pie(gender_counts.values, labels=gender_counts.index,
        autopct='%1.1f%%', startangle=90)
ax2.axis('equal')

root = tk.Tk()
canvas = FigureCanvasTkAgg(fig2, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

button = tk.Button(root, text="Refresh", command=update_chart)
button.pack()

tk.mainloop()




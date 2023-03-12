
from tkinter import ROUND
import random
nama_kating = input("Masukan Nama Kating:")

tingkat_cocok = round(random.uniform(0.1, 1), 1)
print(tingkat_cocok)

# range nilai
if tingkat_cocok > 0.8:
    print(f"Kamu sangat cocok dengan {nama_kating}!")
elif 0.5 <= tingkat_cocok <= 0.8:
    print(f"kamu lumayan cocok dengan {nama_kating}!")
else:
    print(f"Kamu tidak cocok dengan {nama_kating}!")

from tkinter import Label, Tk
import time
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter.font import *
import os


# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Kuy nge-GUI!")
#         master.geometry("500x300")
#         self.label = Label(master, text="Contoh GUI Python zaman now!")
#         self.label.pack()
#         self.greet_button = Button(
#             master, text="Sapo", command=self.sapa, bg='blue')
#         self.greet_button.pack()
#         self.close_button = Button(
#             master, text="Keluar", command=master.destroy, bg='red')
#         self.close_button.pack()

#     def sapa(self):
#         master = Toplevel(self.master)
#         Label(master, text="Haloooooo!").pack()


# class Penghitung:
#     def __init__(self, master):
#         self.master = master
#         master.title('test')
#         master.geometry("300x100")
#         self.hitungan = 0
#         self.label = Label(master, text=self.hitungan)
#         self.label.pack()
#         self.tambah_button = Button(
#             master, text="Tambah", command=self.tambah, bg="#00FF00")
#         self.tambah_button.pack()
#         self.kurang_button = Button(
#             master, text="Kurang", command=self.kurang, bg="#FF0000")
#         self.kurang_button.pack()

#     def tambah(self):
#         master = Toplevel(self.master)
#         Label(master, text=self.hitungan).pack()

#     def tambah(self):
#         self.hitungan += 1
#         self.label['text'] = self.hitungan

#     def kurang(self):
#         self.hitungan -= 1
#         self.label['text'] = self.hitungan

# class Formulirku:
#     def __init__(self, master):
#         self.master = master
#         master.title("Kuy nge-GUI!")
#         self.label = Label(master, text="Halo, nama saya..")
#         self.label.pack()
#         self.nama = StringVar()
#         self.field_nama = Entry(master, textvariable=self.nama, width=40)
#         self.field_nama.pack()
#         self.button = Button(master, text="OK", command=self.edit_nama)
#         self.button.pack()

#     def edit_nama(self):
#         showinfo(message="Halo, {}!".format(self.nama.get()))


# class DaftarMhs():
#     daftar_mhs = []

#     def __init__(self, master):
#         self.master = master
#         master.title("Daftar Mahasiswa")
#         master.geometry("350x500")
#         self.label = Label(master, text="Masukkan nama mhs:")
#         self.label.pack()
#         self.nama = StringVar()
#         self.field_nama = Entry(master, textvariable=self.nama, width=40)
#         self.field_nama.pack()
#         self.button = Button(master, text="Daftarkan",
#                              command=self.daftar)
#         self.button.pack()
#         self.button = Button(master, text="keluarkan",
#                              command=self.hapus)
#         self.button.pack()

#     def daftar(self):
#         mhs = self.nama.get()
#         DaftarMhs.daftar_mhs.append(mhs)
#         showinfo(message="{} berhasil didaftarkan!\n\nDaftar mahasiswa menjadi:\n{}".format(
#             mhs, DaftarMhs.daftar_mhs))
#         self.nama.set("")

#     def hapus(self):
#         mhs = self.nama.get()

#         DaftarMhs.daftar_mhs.remove(mhs)
#         showinfo(message="{} berhasil dikeluarkan!\n\nDaftar mahasiswa menjadi:\n{}".format(
#             mhs, DaftarMhs.daftar_mhs))
#         self.nama.set("")


# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Kuy nge-GUI!")
#         img = ImageTk.PhotoImage(Image.open(
#             'C:/Users/acer/Downloads/217299864.jpg'))
#         self.label = Label(image=img)
#         self.label.image = img
#         self.label.pack()


# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         menubar = Menu(master)
#         master['menu'] = menubar

#         block_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Menu 1", menu=block_menu)
#         block_menu.add_command(label="Command 1.1")
#         block_menu.add_command(label="Command 1.2")
#         block_menu2 = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Menu 2", menu=block_menu2)
#         block_menu2.add_command(label="Command 2.1")


class DaftarMhs:
    def __init__(self, master):
        self.master = master
        master.title("Daftar Mahasiswa")
        master.geometry("350x150")
        font_message = Font(family='Courier New', size=10, weight='bold')
        self.label = Label(
            master, text="Masukkan Nama Kamu", font=font_message)
        self.label.pack()
        self.nama = StringVar()
        self.field_nama = Entry(master, textvariable=self.nama, width=40)
        self.field_nama.pack()

        self.label = Label(master, text="NIM", font=font_message)
        self.label.pack()

        self.nim = StringVar()
        self.field_kelas = Entry(master, textvariable=self.nim, width=40)
        self.field_kelas.pack()

        self.button1 = Button(master, text="input", command=self.input)
        self.button1.pack()

    def input(self):
        nama_mhs = self.nama.get()
        nim = self.nim.get()
        showinfo(
            message=f"hello {nama_mhs}\n\n dengan nim {nim}")
        self.nim.set("")


class Daftarmhs2:
    def __init__(self, master):
        self.master = master
        master.title('Daftar Mahasiswa')
        master.geometry('350x150')

        self.label1 = Label(master, text='Masukkan Nama Panjang:',
                            anchor='e', width=20).grid(row=0, column=0)
        self.label1 = StringVar()
        self.fieldlabel1 = Entry(
            master, textvariable=self.label1, width=30).grid(row=0, column=1)
        self.label2 = Label(master, text='Masukkan NIM:',
                            anchor='c', width=20).grid(row=1, column=0)
        self.label2 = StringVar()
        self.fieldlabel2 = Entry(
            master, textvariable=self.label2, width=30).grid(row=1, column=1)
        Button(master, text="input", command=self.input).grid(row=2, column=1)

    def input(self):
        nama = self.label1.get()
        nama1 = nama.split()
        kelas1 = self.label2.get()
        kelas2 = kelas1
        if int(kelas2[-1]) % 2 == 0:
            kelas2 = '2022B'
        else:
            kelas2 = '2022A'
        showinfo(
            message=f"hello {nama1[0]}\n\n dengan nim {kelas1} kamu pasti dari kelas {kelas2} kan !")


class penjumlahanfix:
    def __init__(self, master):
        hasil = 0
        self.master = master
        master.title("Aplikasi Penjumlahan ")
        master.geometry('350x150')
        label_font = Font(family='Courier New', size=10, weight='bold')
        label_font1 = Font(family='Times', size=10)
        label_font2 = Font(family='Times', size=10, weight='bold')
        lbl = Label(master, text="Masukkan Nilai Pertama : ", font=label_font1,
                    anchor="e", width=20)
        lbl.grid(column=0, row=0)
        self.nilai1 = Entry(master, width=10)
        self.nilai1.grid(column=1, row=0)
        lbl2 = Label(master, text="Masukkan Nilai Kedua : ", font=label_font1,
                     anchor="e", width=20)
        lbl2.grid(column=0, row=2)
        lblplus = Label(master, text='+', font=label_font1)
        lblplus.grid(column=1, row=1)
        self.nilai2 = Entry(master, width=10)
        self.nilai2.grid(column=1, row=2)
        lbl3 = Label(master, text="Hasil : ",
                     font=label_font2, anchor="e", width=20)
        lbl3.grid(column=0, row=3)
        btn = Button(master, text="Tambah",
                     font=label_font, command=self.tambah)
        btn.grid(column=2, row=3)
        self.hasil = Label(master, text=hasil, anchor="c", width=10)
        self.hasil.grid(column=1, row=3)

    def tambah(self):
        self.hasil.configure(
            text=(int(self.nilai1.get())+int(self.nilai2.get())))


class coba:
    def menu(self):
        # self.pilihan_angka = pilihan_angka
        list = [1, 2, 3, 4]
        list2 = ['Nomer 1', 'Nomer 2', 'Nomer 3', 'EXIT']
        print('Pilih Soal')
        for val1, val2 in zip(list, list2):
            print(f'{val1}.{val2}')
        self.pilihan_angka = int(input())
        os.system('cls')
        self.jika()

    def jika(self):
        if self.pilihan_angka == 1:
            self.nomer1()
        elif self.pilihan_angka == 2:
            self.nomer2()
        elif self.pilihan_angka == 3:
            self.nomer3()
        elif self.pilihan_angka == 4:
            os.system('cls')
            exit
            self.nomer3()
        else:
            print('pilihan tidak tersedia')
            input('press enter to continue')
            os.system('cls')
            self.menu()

    def nomer1(self):
        root = Tk()
        my_gui = DaftarMhs(root)
        root.mainloop()

    def nomer2(self):
        root = Tk()
        my_gui = Daftarmhs2(root)
        root.mainloop()

    def nomer3(self):
        root = Tk()
        my_gui = penjumlahanfix(root)
        root.mainloop()


app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


lu = coba()
i = lu.menu()

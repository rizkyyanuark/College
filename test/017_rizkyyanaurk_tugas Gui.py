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
        self.field_nama = Entry(master, width=40)
        self.field_nama.pack()
        self.label = Label(master, text="NIM", font=font_message)
        self.label.pack()
        self.field_kelas = Entry(master, width=40)
        self.field_kelas.pack()
        self.button1 = Button(master, text="input",
                              bg='#4bd863', command=self.input)
        self.button1.pack()

    def input(self):
        nama_mhs = self.field_nama.get()
        nim = self.field_kelas.get()
        showinfo(
            message=f"hello {nama_mhs}\n\n dengan nim {nim}")


class helloMhs_v2:
    def __init__(self, master):
        self.master = master
        master.title("Hello Mahasiswa")
        master.geometry("450x500")

        self.nama = Label(
            master, text="Masukkan Nama Panjang").grid(row=1, column=3)
        self.label1 = Entry(
            master)
        self.label1.grid(row=1, column=4)
        self.kelas_nim = Label(
            master, text="Masukkan NIM").grid(row=2, column=3)
        self.label2 = Entry(
            master)
        self.label2.grid(row=2, column=4)
        Button(master, text="Input",
               command=self.input).grid(row=3, column=4)

    def input(self):
        nama = self.label1.get()
        nama1 = nama.split()
        kelas1 = self.label2.get()
        kelas2 = kelas1
        if int(kelas2[-1]) % 2 == 0:
            kelas2 = ('2022B')
        else:
            kelas2 = ('2022A')
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
        lbl = Label(master, text="Masukan Nilai Pertama : ", font=label_font1,
                    anchor="e", width=20)
        lbl.grid(column=0, row=0)
        self.nilai1 = Entry(master, width=10)
        self.nilai1.grid(column=1, row=0)
        lbl2 = Label(master, text="Masukan Nilai Kedua : ", font=label_font1,
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


def nomer1():
    root = Tk()
    my_gui = DaftarMhs(root)
    root.mainloop()


def nomer2():
    root = Tk()
    my_gui = helloMhs_v2(root)
    root.mainloop()


def nomer3():
    root = Tk()
    my_gui = penjumlahanfix(root)
    root.mainloop()


master = Tk()
master.title("Tk GUI ANIME")
master.geometry("350x150")
master.configure(bg="white")
buton1 = Button(master, text='Nomer 1', command=nomer1)
buton1.pack()
buton2 = Button(master, text='Nomer 2', command=nomer2)
buton2.pack()
buton3 = Button(master, text='Nomer 3', command=nomer3)
buton3.pack()
master.mainloop()

# class coba:
#     def __init__(self, pilihan_angka):
#         self.pilihan_angka = pilihan_angka

#     def jika(self):
#         if self.pilihan_angka == 1:
#             self.nomer1()
#         elif self.pilihan_angka == 2:
#             self.nomer2()
#         elif self.pilihan_angka == 3:
#             self.nomer3()
#         else:
#             print('pilihan tidak tersedia')
#             input('press enter to continue')


# list = [1, 2, 3]
# list2 = ['Nomer 1', 'Nomer 2', 'Nomer 3']
# for val1, val2 in zip(list, list2):
#     print(f'{val1}.{val2}')
# x = int(input())
# os.system('cls')
# lu = coba(x)
# i = lu.jika()

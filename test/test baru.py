from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from tkinter import *
import tkinter as tk
from tkinter.font import *
import os


class radiobutton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.nilai = IntVar()
        self.nama = []
        self.nilai.set(0)
        rb_mahasiswa = tk.Radiobutton(
            self, text="Mahasiswa", variable=self.nilai, value=1).place(x=20, y=20)
        rb_dosen = tk.Radiobutton(
            self, text="Dosen", variable=self.nilai, value=2).place(x=25, y=25)
        rb_umum = tk.Radiobutton(
            self, text="Umum", variable=self.nilai, value=0).place(x=150, y=30)
        buton = tk.Button(self, text='Input',
                          command=self.input).place(x=200, y=200)

    def input(self):
        nilai = self.nilai.get()
        if nilai == 1:
            self.openmahasiswa()
        elif nilai == 2:
            self.opendosen()
        else:
            self.openumum()

    def openmahasiswa(self):
        mahasiswa(self)

    def opendosen(self):
        dosen(self)

    def openumum(self):
        umum(self)


class mahasiswa(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label1 = tk.Label(
            self, text="Silahkan masukkan formulir ini:", anchor='e')
        label1.pack()
        label2 = tk.Label(
            self, text="Nama", anchor='e')
        label2.pack()
        entry1 = self.nama = tk.Entry(
            self)
        entry1.pack()
        label3 = tk.Label(
            self, text="NIM", anchor='w')
        label3.pack()
        entry2 = self.nim = tk.Entry(
            self)
        entry2.pack()
        label4 = tk.Label(
            self, text="Email", anchor='w')
        label4.pack()
        entry3 = self.email = tk.Entry(
            self)
        entry3.pack()
        label5 = tk.Label(
            self, text="Instansi", anchor='w')
        label5.pack()
        entry4 = self.instansi = tk.Entry(
            self)
        entry4.pack()
        button1 = tk.Button(self, text="Input", command=self.submit)
        button1.pack()

    def submit(self):
        nama1 = self.nama.get()
        nim1 = self.nim.get()
        email1 = self.email.get()
        instansi1 = self.instansi.get()
        showinfo(
            message=f'Terimakasih, data anda telah tersimpan\nNama:{nama1}\nnim: {nim1}\nEmail: {email1}\nInstansi: {instansi1}')


class dosen(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        label1 = tk.Label(
            self, text="Silahkan masukkan formulir ini:", anchor='e')
        label1.pack()
        label2 = tk.Label(
            self, text="Nama", anchor='e')
        label2.pack()
        entry1 = self.nama = tk.Entry(
            self)
        entry1.pack()
        label4 = tk.Label(
            self, text="Email", anchor='w')
        label4.pack()
        entry3 = self.email = tk.Entry(
            self)
        entry3.pack()
        label5 = tk.Label(
            self, text="Instansi", anchor='w')
        label5.pack()
        entry4 = self.instasi = tk.Entry(
            self)
        entry4.pack()
        button1 = tk.Button(self, text="Input", command=self.submit)
        button1.pack()

    def submit(self):
        nama1 = self.nama.get()
        email1 = self.email.get()
        instansi1 = self.instansi.get()
        showinfo(
            message=f'Terimakasih, data anda telah tersimpan\nNama:{nama1}\nEmail: {email1}\nInstansi: {instansi1}')


class umum(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        label1 = tk.Label(
            self, text="Silahkan masukkan formulir ini:", anchor='e')
        label1.pack()
        label2 = tk.Label(
            self, text="Nama", anchor='e')
        label2.pack()
        entry1 = self.nama = tk.Entry(
            self)
        entry1.pack()
        label4 = tk.Label(
            self, text="Email", anchor='w')
        label4.pack()
        entry3 = self.email = tk.Entry(
            self)
        entry3.pack()
        button1 = tk.Button(self, text="Input", command=self.submit)
        button1.pack()
        label = tk.Label(self, text="umum")
        label.pack(padx=50, pady=50)

    def submit(self):
        nama1 = self.nama.get()
        email1 = self.email.get()
        showinfo(
            message=f'Terimakasih, data anda telah tersimpan\nNama:{nama1}\nEmail: {email1}')


main = radiobutton()
main.mainloop()

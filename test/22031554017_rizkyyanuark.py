from tkinter import *
root = Tk()
root.title("Absensi Perkuliahan")
root.geometry('300x200')


def clear():
    pertama.set('')
    kedua.set('')


def input():
    kamus = {1: 'satu', 2: 'dua', 3: 'tiga', 4: 'empat', 5: 'lima', 6: 'enam', 7: 'tujuh', 8: 'depalan', 9: 'sembilan', 10: 'sepuluh',
             11: 'sebelas',
             12: 'dua belas',
             13: 'tiga belas',
             14: 'empat belas',
             15: 'lima belas',
             16: 'enam belas',
             17: 'tujuh belas',
             18: 'delapan belas',
             19: 'sembilan belas', 20: 'dua puluh'}

    jawa = {1: "setunggal",
            2: "kaleh",
            3: "tigo",
            4: "sekawan",
            5: "gangsal",
            6: "enem",
            7: "pitu",
            8: "wolu",
            9: "songo",
            10: "sedoso",
            11: "sewelas",
            12: "kalehwelas",
            13: "tigowelas",
            14: "sekawanwelas",
            15: "ganggsalwelas",
            16: "nembelas",
            17: "pitulas",
            18: "wolulas",
            19: "songolas",
            20: "kalehdoso"}
    angka1 = angka.get()
    clear()
    if angka1 <= 20:
        if angka1 in kamus:
            if angka1 in jawa:
                pertama.set(kamus[angka1])
                kedua.set(jawa[angka1])
    else:
        lbl1.config(text='data tidak ada')


        # print(f'{angka}\n>>> {kamus[angka]} = {jawa[angka]}')
angka = IntVar()
pertama = StringVar()
kedua = StringVar()
lbl = Label(root, text="Masukkan Nama Kamu")
lbl.pack()
field_nama = Entry(root, textvariable=angka, width=40)
field_nama.pack()
button1 = Button(root, text="input", bg='#4bd863', command=input)
button1.pack()
lbl1 = Entry(root, textvariable=pertama)
lbl1.pack()
lbl2 = Entry(root, textvariable=kedua)
lbl2.pack()

root.mainloop()

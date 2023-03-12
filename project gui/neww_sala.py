# import modul
from tkinter import *
import math
import tkinter.messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

######################################################################################################################

root = Tk()
root.title("Kalkulator Scientific")  # menetapkan nama judul di bagian atas GUI
root.configure(bg='white')  # mengatur warna latar belakang kalkulator
# pengguna tidak akan dapat menyesuaikan ukurannya, jadi ukurannya akan tetap
root.resizable(width=False, height=False)
root.geometry("480x550+450+70")  # mengatur ukuran dalam pixel
calc = Frame(root)  # frame/ wadah untuk angka dan operator
calc.grid()  # membuat kisi seperti pola bingkai

######################################################################################################################

# Sekarang kita akan membuat kelas di mana kita akan membuat kelas yang akan membuat semua
# fungsi dari kalkulator scientific, sehingga dapat dipanggil dan dijalankan dengan mudah


class Calc():
    def __init__(self):
        self.total = ''
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)


class PersamaanKuadrat:

    def __init__(self, parent, title):
        self.parent = parent

        # self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)

        self.aturKomponen()

        self.entP2.focus_set()

    def aturKomponen(self):
        # atur frame utama
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        self.kopangkat2 = IntVar()
        self.kopangkat1 = IntVar()
        self.kopangkat0 = IntVar()
        # Label Rumus
        Label(mainFrame, text="Menghitung Akar-akar Persamaan Kuadrat").grid(
            row=0, column=0, columnspan=2)
        Label(mainFrame, text="AX^2 + BX + C = 0", fg="red").grid(row=1, column=0,
                                                                  pady=10, columnspan=2)

        # input data:
        Label(mainFrame, text="Koefisien pangkat 2:").grid(
            row=2, column=0, sticky=W)
        self.entP2 = Entry(mainFrame, textvariable=self.kopangkat2, width=5)
        self.entP2.grid(row=2, column=1, sticky=W)

        Label(mainFrame, text="Koefisien pangkat 1:").grid(
            row=3, column=0, sticky=W)
        self.entP1 = Entry(mainFrame, textvariable=self.kopangkat1, width=5)
        self.entP1.grid(row=3, column=1, sticky=W)

        Label(mainFrame, text="Koefisien pangkat 0:").grid(
            row=4, column=0, sticky=W)
        self.entP0 = Entry(mainFrame, textvariable=self.kopangkat0, width=5)
        self.entP0.grid(row=4, column=1, sticky=W)

        # tombol CARI AKAR!
        self.btnCariAkar = Button(mainFrame, text="CARI AKAR!",
                                  command=self.onCariAkar)
        self.btnCariAkar.grid(row=5, column=0, columnspan=2, pady=10)

        # output data / nilai akar
        Label(mainFrame, text="Nilai akar X1:").grid(
            row=6, column=0, sticky=W)
        self.entX1 = Entry(mainFrame)
        self.entX1.grid(row=6, column=1, sticky=W)

        Label(mainFrame, text="Nilai akar X2:").grid(
            row=7, column=0, sticky=W)
        self.entX2 = Entry(mainFrame)
        self.entX2.grid(row=7, column=1, sticky=W)

    def onCariAkar(self, event=None):
        A = float(self.kopangkat0.get())
        B = float(self.kopangkat1.get())
        C = float(self.kopangkat2.get())

        # membersihkan entry X1 dan X2
        self.entX1.delete(0, END)
        self.entX2.delete(0, END)

        dua_A = 2.0 * A
        # mencari diskriminan
        disk = B*B - 4*A*C

        if disk > 0:
            akarDisk = math.sqrt(disk)
            akar1 = (-B + akarDisk)/dua_A
            akar2 = (-B - akarDisk)/dua_A

            self.entX1.insert(END, str(akar1))
            self.entX2.insert(END, str(akar2))

        elif disk == 0:
            akar1 = -B/dua_A
            akar2 = akar1

            self.entX1.insert(END, str(akar1))
            self.entX2.insert(END, str(akar2))

        else:
            akar1 = -B/dua_A
            akar11 = math.sqrt(abs(disk))/dua_A
            akar2 = akar1
            akar12 = -akar11

            self.entX1.insert(END, str(akar1)+" + "+str(abs(akar12))+" i")
            self.entX2.insert(END, str(akar2)+" - "+str(abs(akar12))+" i")

    def onKeluar(self, event=None):
        self.parent.destroy()


def abcformula():
    root = Tk()

    aplikasi = PersamaanKuadrat(root, "ABC Formula")

    # root.mainloop()


added_value = Calc()

######################################################################################################################

# Kode di bawah ini akan membuat tampilan di GUI kalkulator dengan menambahkan gaya font, ukuran font,
# warna latar belakang, warna latar depan sebagai argumen di dalam fungsi entry.
txtDisplay = Entry(calc, font=('Yu Gothic UI', 19),
                   bg='#eadbc9', fg='black',
                   bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

######################################################################################################################


numberpad = "123456789"  # menyimpan semua angka dalam variabel

i = 0  # Di sini berfungsi untuk menghitung baris untuk menempatkan tombol di kisi

btn = []  # buat daftar kosong untuk disimpan
# setiap tombol dengan spesifikasi khususnya

for j in range(2, 5):  # j is in that range to place the button in that particular row
    for k in range(3):  # k is in this range to place the button in that particular column
        btn.append(Button(calc, width=6, height=2,
                          bg='#DAD3F2', fg='#B45400',
                          font=('Helvetica', 20, 'bold'),
                          bd=4, text=numberpad[i]))

        # mengatur tombol di baris & kolom dan pisahkan dengan padding 1 unit
        btn[i].grid(row=j, column=k, pady=1)

        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1  # put that number as a symbol on that button

######################################################################################################################

# Sekarang kita akan menempatkan semua tombol / operator di posisi masing-masing di grid.
# untuk mengaturnya sesuai pilihan pribadi masing" dengan mengubah nilai baris dan kolomnya.
# Dalam hal ini, setiap fungsi tombol hanya mengambil nama operator, lebar, tinggi, latar belakang, latar depan, font,
# dan posisi kolom & baris masing-masing tombol sebagai argumen.
btnClear = Button(calc, text=chr(67), width=6,
                  height=2, bg='#E7C7DC', fg='#DC7092',
                  font=('Helvetica', 20, 'bold'), bd=4, command=added_value.Clear_Entry
                  ).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='#E7C7DC', fg='#DC7092',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.All_Clear_Entry
                     ).grid(row=1, column=1, pady=1)

btnsq = Button(calc, text="\u221A", width=6, height=2,
               bg='#E7C7DC', font=('Helvetica', 20, 'bold'), fg='#DC7092',
               bd=4, command=added_value.squared
               ).grid(row=1, column=2, pady=1)

btnTambah = Button(calc, text="+", width=6, height=2,
                   bg='#E7C7DC', fg='#DC7092',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=lambda: added_value.operation("add")
                   ).grid(row=1, column=3, pady=1)

btnKurang = Button(calc, text="-", width=6,
                   height=2, bg='#E7C7DC', fg='#DC7092',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=lambda: added_value.operation("sub")
                   ).grid(row=2, column=3, pady=1)

btnKali = Button(calc, text="x", width=6,
                 height=2, bg='#E7C7DC', fg='#DC7092',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.operation("multi")
                 ).grid(row=3, column=3, pady=1)

btnBagi = Button(calc, text="/", width=6,
                 height=2, bg='#E7C7DC', fg='#DC7092',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.operation("divide")
                 ).grid(row=4, column=3, pady=1)

btn0 = Button(calc, text="0", width=6,
              height=2, bg='#DAD3F2', fg='#B45400',
              font=('Helvetica', 20, 'bold'),
              bd=4, command=lambda: added_value.numberEnter(0)
              ).grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.numberEnter(".")
                ).grid(row=5, column=1, pady=1)

btnPM = Button(calc, text=chr(177), width=6, fg='#DC7092',
               height=2, bg='#E7C7DC', font=('Helvetica', 20, 'bold'),
               bd=4, command=added_value.mathPM
               ).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=6,
                   height=2, bg='#E7C7DC', fg='#DC7092',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.sum_of_total
                   ).grid(row=5, column=3, pady=1)
# ROW 1 :
btnPhi = Button(calc, text="π", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.pi
                ).grid(row=1, column=4, pady=1)

btnCos = Button(calc, text="Cos", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.cos
                ).grid(row=1, column=5, pady=1)

btntan = Button(calc, text="tan", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.tan
                ).grid(row=1, column=6, pady=1)

btnsin = Button(calc, text="sin", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.sin
                ).grid(row=1, column=7, pady=1)


# ROW 2 :
btn2Pi = Button(calc, text="2π", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.tau
                ).grid(row=2, column=4, pady=1)

btnCosh = Button(calc, text="Cosh", width=6,
                 height=2, bg='#DAD3F2', fg='#B45400',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.cosh
                 ).grid(row=2, column=5, pady=1)

btntanh = Button(calc, text="tanh", width=6,
                 height=2, bg='#DAD3F2', fg='#B45400',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.tanh
                 ).grid(row=2, column=6, pady=1)

btnsinh = Button(calc, text="sinh", width=6,
                 height=2, bg='#DAD3F2', fg='#B45400',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.sinh
                 ).grid(row=2, column=7, pady=1)

# ROW 3 :
btnlog = Button(calc, text="log", width=6,
                height=2, bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.log
                ).grid(row=3, column=4, pady=1)

btnlog2 = Button(calc, text="log2", width=6,
                 height=2, bg='#DAD3F2', fg='#B45400',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.log2
                 ).grid(row=3, column=5, pady=1)

btnlog10 = Button(calc, text="log10", width=6,
                  height=2, bg='#DAD3F2', fg='#B45400',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.log10
                  ).grid(row=3, column=6, pady=1)

btnlog1p = Button(calc, text="log1p", width=6,
                  height=2, bg='#DAD3F2', fg='#B45400',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.log1p
                  ).grid(row=3, column=7, pady=1)

# ROW 4 :
btnExp = Button(calc, text="exp", width=6, height=2,
                bg='#E7C7DC', fg='#DC7092',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.exp
                ).grid(row=4, column=4, pady=1)

btndeg = Button(calc, text="deg", width=6,
                height=2, bg='#DAD3F2', fg='#B45400',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.degrees
                ).grid(row=4, column=5, pady=1)

btnMod = Button(calc, text="Mod", width=6,
                height=2, bg='#DAD3F2', fg='#B45400',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("mod")
                ).grid(row=4, column=6, pady=1)

btnE = Button(calc, text="e", width=6,
              height=2, bg='#DAD3F2', fg='#B45400',
              font=('Helvetica', 20, 'bold'),
              bd=4, command=added_value.e
              ).grid(row=4, column=7, pady=1)

# ROW 5 :
btnacosh = Button(calc, text="acosh", width=6,
                  height=2, bg='#E7C7DC', fg='#DC7092',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.acosh
                  ).grid(row=5, column=4, pady=1)

btnasinh = Button(calc, text="asinh", width=6,
                  height=2, bg='#E7C7DC', fg='#DC7092',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.asinh
                  ).grid(row=5, column=5, pady=1)

btnexpm1 = Button(calc, text="expm1", width=6,
                  height=2, bg='#E7C7DC', fg='#DC7092',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.expm1
                  ).grid(row=5, column=6, pady=1)

btngamma = Button(calc, text="gamma", width=6,
                  height=2, bg='#E7C7DC', fg='#DC7092',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.lgamma
                  ).grid(row=5, column=7, pady=1)

lblDisplay = Label(calc, text="Scientific Calculator",
                   font=('Yu Gothic UI', 30, 'bold'),
                   bg='white', fg='black', justify=CENTER)

lblDisplay.grid(row=0, column=4, columnspan=4)

######################################################################################################################

# Gunakan fungsi askyesno untuk menghentikan / lanjutkan eksekusi program


def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Scientific Calculator", "Anda yakin ingin keluar ?")
    if iExit > 0:
        root.destroy()  # otomatis keluar
        return


def Viewhelp():
    Help = tkinter.messagebox.askyesno(
        'Bantuan', 'Halo, untuk bantuan dan saran Anda bisa menghubungi 085852011597')
    if Help > 0:
        root.destroy()


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("1000x568+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x560+0+0")


def ABCFormula():
    root.resizable(width=False, height=False)
    root.geometry("1000x568+0+0")


######################################################################################################################
# membuat bagian grafik
def Grafik():
    # memasukkan grafikwindow ke dalam fungsi root
    grafikWindow = Toplevel(root)
    grafikWindow.title("Aplikasi Grafik Trigonometri")  # membuat judul
    # windows resolution tidak bisa diperbesar atau diperkecil
    grafikWindow.resizable(width=False, height=False)

    WIDTH = 700
    HEIGHT = 600
    canvas = Canvas(grafikWindow, width=WIDTH, height=HEIGHT, bg='#eadbc9')
    canvas.pack()

    # fungsi untuk mengaktifkan button enter pada grafik
    def inputgrafik():
        a = int(aInput.get())
        b = int(bInput.get())
        c = int(cInput.get())

        # membuat vektor baris berisi n titik yang terpisah merata secara linier
        x = np.linspace(-50, 50, 10)

        if yInput.get() == yvalues[0]:
            y = c + a*(np.sin(x)**b)
            ax.plot(x, y)
        if yInput.get() == yvalues[1]:
            y = c + a*(np.cos(x)**b)
            ax.plot(x, y)
        if yInput.get() == yvalues[2]:
            y = c + a*(np.tan(x)**b)
            ax.plot(x, y)

        canvasGrafik.draw()

        # visualisasi input
    frameInput = Frame(grafikWindow, bg='#c49f9f')
    frameInput.place(relx=0.025, rely=0.5, relwidth=0.25,
                     relheight=0.7, anchor='w')

    yvalues = ("c + a sin(x)^b",
               "c + a cos(x)^b",
               "c + a tan(x)^b")

    ylabel = Label(frameInput, bg='#c49f9f', text='y', fg='white')
    ylabel.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.125, anchor='n')
    yInput = Spinbox(frameInput, values=yvalues)
    yInput.place(relx=0.5, rely=0.025, relwidth=0.6,
                 relheight=0.08, anchor='n')

    alabel = Label(frameInput, bg='#c49f9f', text='a', fg='white')
    alabel.place(relx=0.1, rely=0.125, relwidth=0.2,
                 relheight=0.125, anchor='n')
    aInput = Entry(frameInput)
    aInput.place(relx=0.5, rely=0.15, relwidth=0.6, relheight=0.08, anchor='n')
    aInput.insert(0, 1)

    blabel = Label(frameInput, bg='#c49f9f', text='b', fg='white')
    blabel.place(relx=0.1, rely=0.25, relwidth=0.2,
                 relheight=0.125, anchor='n')
    bInput = Entry(frameInput)
    bInput.place(relx=0.5, rely=0.275, relwidth=0.6,
                 relheight=0.08, anchor='n')
    bInput.insert(0, 1)

    clabel = Label(frameInput, bg='#c49f9f', text='c', fg='white')
    clabel.place(relx=0.1, rely=0.375, relwidth=0.2,
                 relheight=0.125, anchor='n')
    cInput = Entry(frameInput)
    cInput.place(relx=0.5, rely=0.4, relwidth=0.6, relheight=0.08, anchor='n')
    cInput.insert(0, 0)

    enter_button = Button(frameInput, text='Enter', command=inputgrafik)
    enter_button.place(relx=0.5, rely=0.7, relwidth=0.3,
                       relheight=0.1, anchor='n')

    frameGrafik = Frame(grafikWindow, bg='white')
    frameGrafik.place(relx=1, rely=0.5, relwidth=0.7, relheight=1, anchor='e')

    # untuk memunculkan visual grafik
    f = Figure()
    ax = f.add_subplot(111)

    ax.set_title('Grafik trigonometri')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # ax.grid(True)

    canvasGrafik = FigureCanvasTkAgg(f, frameGrafik)
    canvasGrafik.get_tk_widget().place(relheight=1, relwidth=1)
    canvasGrafik.draw()

######################################################################################################################


# Membuat menubar dari calculator GUI
menubar = Menu(calc)

# MenuBar 1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Calc', menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_command(label="ABCFormula", command=abcformula)
filemenu.add_separator()  # garis pemisah
filemenu.add_command(label="Exit", command=iExit)

# MenuBar 2 :
grafikmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Grafik', menu=grafikmenu)
grafikmenu.add_command(label="Grafik", command=Grafik)

# MenuBar 3 :
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help', command=Viewhelp)


root.config(menu=menubar)
root.mainloop()

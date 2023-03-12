import os


class test():

    def next(self):
        print('press enter to continue')
        x = input()
        os.system('cls')
    # No 1

    def __init__(self, name, age):
        self.name = name
        self.umur = age

    def biodata(self):
        print('NAMA:', self.name)
        print('USIA:', self.umur)
        print("Selamat Datang!")
        self.next()
        self.penjumlahan()

    # NO 2
    def penjumlahan(self):
        print('NO 2')
        print("Masukkan angka pertama: ")
        angka1 = int(input())
        print("Masukkan angka pertama: ")
        angka2 = int(input())
        print(f'jumlah dari {angka1} + {angka2} adalah {angka1 + angka2}')
        self.next()
        self.pengurangan()

    def pengurangan(self):
        print('NO 2')
        print("Masukkan angka pertama: ")
        angka1 = int(input())
        print("Masukkan angka pertama: ")
        angka2 = int(input())
        print(f'jumlah dari {angka1} - {angka2} adalah {angka1 - angka2}')
        self.next()
        self.nilai_max()

    # NO 3
    def nilai_max(self):
        print('NO 3')
        list = []
        print("Masukkan list angka :")
        x = int(input())
        for i in range(0, x):
            angka = int(input())
            list.append(angka)
        print(list)
        print('Nilai terbesar:', max(list))
        self.next()
        self.max()

    # NO 4
    def max(self):
        print('NO 4')
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        c = int(input("Masukkan angka ketiga: "))
        d = int(input("Masukkan angka keempat: "))
        e = int(input("Masukkan angka kelima: "))
        print(
            f'nilai terbesar dari {a},{b},{c},{d},{e} adalah {max(a, b, c, d, e)}')
        self.next()
        self.sumofVocalnConsonant()

    # NOMOR 5
    def sumofVocalnConsonant(self):
        print('NO 5')
        vocal = 0
        consonant = 0
        s = input()
        for i in s:
            if i in "aiueoAIUEO":
                vocal += 1
            else:
                consonant += 1
        print(f'jumlah huruf vocal {vocal}, sedangkan konsonan {consonant}')


# input no 1
print('Masukkan Nama Anda')
name = input()
print('Masukkan Usia Anda')
age = input()
os.system('cls')
l1 = test(name, age)
l = l1.biodata()

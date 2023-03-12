import os

# no 4


# class attendee():
#     def __init__(self, nama, nim, absen):
#         self.name = nama
#         self.id = nim
#         self.total = absen

#     def menu(self):
#         os.system('cls')
#         print(f'Selamat Datang {self.name}!')

#         print('1.Masuk Zoom')
#         print('2.keluar Zoom')
#         print('silahkan pilih')
#         choice = int(input())
#         os.system('cls')
#         if choice == 1:
#             print(f'{self.name} telah masuk zoom')
#             self.total += 1
#             print(f'jumlah orang yang sedang rapat {self.total}')
#             self.test()
#         elif choice == 2:
#             print(f'{self.name} telah keluar zoom')
#             if self.total == 0:
#                 print(f'jumlah orang yang sedang rapat 0')
#                 self.test()
#             else:
#                 self.total -= 1
#                 print(f'jumlah orang yang sedang rapat {self.total}')
#                 self.test()
#         else:
#             print(f'nomer yang anda masukan tidak ada!')
#             self.test()

#     def test(self):
#         input('press enter to continue')
#         os.system('cls')
#         self.loginagain()

#     def loginagain(self):
#         self.menu()


# absen = 0
# print("Masukkan nama anda: ")
# nama = input()
# print("Masukkan nim anda: ")
# nim = int(input())
# lu = attendee(nama, nim, absen)
# l = lu.menu()


# # no 2
# class pendaftaran():
#     def __init__(self, list, nama, noid, kelahiran, alamat_asal):
#         self.book = list
#         self.name = nama
#         self.id = noid
#         self.kelahiran = kelahiran
#         self.alamat = alamat_asal

#     def list_jurusan(self):
#         print(f'selamat datang {self.name} di unesa')

#         for i in self.book:
#             print(i)
#         self.jurusan = int(input())
#         if self.jurusan == 1:
#             self.jurusan = 'Matematika'
#             self.pilih_prodi()
#         elif self.jurusan == 2:
#             self.jurusan = 'Fisika'
#             self.pilih_prodi()
#         elif self.jurusan == 3:
#             self.jurusan = 'Kimia'
#             self.pilih_prodi()
#         elif self.jurusan == 4:
#             self.jurusan = 'Biologi'
#             self.pilih_prodi()
#         elif self.jurusan == 5:
#             self.jurusan = 'Sains Data'
#             self.pilih_prodi()
#         else:
#             print('pilihan tidak tersedia')
#             input('prees enter to continue')
#             os.system('cls')
#             self.list_jurusan()

#     def pilih_prodi(self):
#         if self.jurusan == 'Matematika':
#             print('1.Matematika murni')
#             print('2.Matematika')
#             self.prodi = int(input())
#             if self.prodi == 1:
#                 self.prodi = 'Matematika Murni'
#                 os.system('cls')
#                 self.pilih_tempat()
#             elif self.prodi == 2:
#                 self.prodi = 'Matematika'
#                 os.system('cls')
#                 self.pilih_tempat()
#             else:
#                 print('pilihan tidaak ada')
#                 input('press enter to continue')
#                 os.system('cls')
#                 self.pilih_prodi()
#         elif self.jurusan == 'Fisika':
#             print('1.Fisika Murni')
#             print('2.Fisika')
#             self.prodi = int(input())
#             if self.prodi == 1:
#                 self.prodi = 'Fisika Murni'
#                 os.system('cls')
#                 self.pilih_tempat()
#             elif self.prodi == 2:
#                 self.prodi = 'Fisika'
#                 os.system('cls')
#                 self.pilih_tempat()
#             else:
#                 print('pilihan tidak tersedia')
#                 input('press enter to continue')
#                 os.system('cls')
#                 self.pilih_prodi()
#         elif self.jurusan == 'Kimia':
#             print('1.Kimia Murni')
#             print('2.Kimia')
#             self.prodi = int(input())
#             if self.prodi == 1:
#                 self.prodi = 'Kimia Murni'
#                 os.system('cls')
#                 self.pilih_tempat()
#             elif self.prodi == 2:
#                 self.prodi = 'Kimia'
#                 os.system('cls')
#                 self.pilih_tempat()
#             else:
#                 print('pilihan tidak tersedia')
#                 input('press enter to continue')
#                 os.system('cls')
#                 self.pilih_prodi()
#             os.system('cls')
#             self.pilih_tempat()
#         elif self.jurusan == 'Biologi':
#             print('1.Biologi Murni')
#             print('2.Biologi')
#             self.prodi = int(input())
#             if self.prodi == 1:
#                 self.prodi = 'Biologi murni'
#                 os.system('cls')
#                 self.pilih_tempat()
#             elif self.prodi == 2:
#                 self.prodi = 'Biologi'
#                 os.system('cls')
#                 self.pilih_tempat()
#             else:
#                 print('pilihan tidak tersedia')
#                 input('press enter to continue')
#                 os.system('cls')
#                 self.pilih_prodi()
#         elif self.jurusan == 'Sains Data':
#             print('1.Sains Data')
#             print('2.Statistik')
#             self.prodi = int(input())
#             if self.prodi == 1:
#                 self.prodi = 'Sains Data'
#                 os.system('cls')
#                 self.pilih_tempat()
#             elif self.prodi == 2:
#                 self.prodi = 'Statistik'
#                 os.system('cls')
#                 self.pilih_tempat()
#             else:
#                 print('pilihan tidak tersedia')
#                 input('press enter to continue')
#                 os.system('cls')
#                 self.pilih_prodi()
#         else:
#             print('pilihan tidak tersedia')
#             input('press enter to continue')
#             os.system('cls')
#             self.list_jurusan()

#     def pilih_tempat(self):
#         print('tulis tempat yang diinginkan')
#         self.pilih_tempat = input()
#         os.system('cls')
#         self.pilihan()

#     def pilihan(self):
#         print(f'Nama\t\t:{self.name}')
#         print(f'NIM\t\t:{self.id}')
#         print(f'Kelahiran\t:{self.kelahiran}')
#         print(f'Jurusan\t\t:{self.jurusan}')
#         print(f'Prodi\t\t:{self.prodi}')
#         print(f'Gedung\t\t:{self.pilih_tempat}')
#         input('press enter to exit')
#         os.system('cls')


# if __name__ == "__main__":
#     list = ['Matematika', 'Fisika',
#             'Kimia', 'Biologi', 'Sains Data']
#     print("Masukkan nama anda")
#     nama = input()
#     print("Masukkan no id anda")
#     noid = input()
#     print("Masukkan kelahiran anda")
#     kelahiran = input()
#     print("Masukkan alamat asal anda")
#     alamat_asal = input()
#     os.system('cls')
#     lu = pendaftaran(list, nama, noid, kelahiran, alamat_asal)
#     l = lu.list_jurusan()


# NO 1
# class persegi_panjang():
#     def __init__(self, nama):
#         self.name = nama

#     def input(self):
#         os.system('cls')
#         self.p = int(input('masukkan panjang:'))
#         self.l = int(input('masukkan lebar:'))

#     def menu(self):
#         print(f'selamat datang {self.name}!')

#         print(f'1.Luas')
#         print(f'2.Keliling')
#         print(f'3.Exit')
#         choice = int(input())
#         if choice == 1:
#             self.luas()
#             return os.system('cls')
#         elif choice == 2:
#             self.keliling()
#             return os.system('cls')
#         elif choice == 3:
#             exit
#         else:
#             print('pilihan tidak tersedia')
#             print('press enter to continue')
#             input()
#             os.system('cls')
#             return self.memu()

#     def luas(self):
#         self.input()
#         hasil = self.p*self.l
#         print(f'Luasnya adalah {hasil}')
#         print('press enter to continue')
#         input()
#         os.system('cls')
#         return self.menu()

#     def keliling(self):
#         self.input()
#         hasil2 = 2*(self.p + self.l)
#         print(f'Kelilingnya adalah {hasil2}')
#         print('press enter to continue')
#         input()
#         os.system('cls')
#         return self.menu()


# print('masukkan nama:')
# x = input()
# os.system('cls')
# lu = persegi_panjang(x)
# i = lu.menu()


#  No 3
class supermarket():
    jumlah_sayur = 0

    def __init__(self, nama, kode, sayur, harga, total, list_baru1, list_baru2):
        self.nama = nama
        self.kode = kode
        self.sayur = sayur
        self.harga = harga
        self.total = total
        self.listbaru1 = list_baru1
        self.listbeli2 = list_baru2
        self.lendict = {}

    def menu2(self):
        print(f'selamat datang {self.nama} di supermarket ')
        print('1.Belanja')
        print('2.Exit')
        choice = int(input())
        if choice == 1:
            os.system('cls')
            self.template1()
        elif choice == 2:
            os.system('cls')
            exit
        else:
            print('pilihan tidak ada')
            input('press enter to continue')
            os.system('cls')
            self.menu2()

    def menu(self):
        print(f'selamat datang {self.nama} di supermarket ')
        print('1.Belanja')
        print('2.list Belanja')
        print('3.Exit')
        choice = int(input())
        if choice == 1:
            os.system('cls')
            self.template1()
        elif choice == 2:
            os.system('cls')
            self.template3()
        elif choice == 3:
            os.system('cls')
            exit
        else:
            print('pilihan tidak ada')
            input('press enter to continue')
            self.menu()

    def template1(self):
        print(f'selamat datang {self.nama} di supermarket ')
        print('=======================')
        for val1, val2, val3 in zip(self.kode, self.sayur, self.harga):
            print(f'{val1}\t{val2}\t{val3}')
        print('=======================')
        self.template2()

    def template3(self):
        print(f'selamat datang {self.nama} di supermarket ')
        print(
            f'jumlah barang = {self.listbeli2} unit')
        print(f'total belanja:\t{self.listbeli1}')
        input('press enter to continue')
        os.system('cls')
        self.menu()

    def template2(self):
        self.item = input('pilih item ')
        self.jumlah_item = self.total + int(input('jumlah item '))
        if self.item == '013':
            self.nama_sayur = 5000*self.jumlah_item
        elif self.item == '015':
            self.nama_sayur = 6000*self.jumlah_item
        elif self.item == '017':
            self.nama_sayur = 3500*self.jumlah_item
        elif self.item == '019':
            self.nama_sayur = 9000*self.jumlah_item
        else:
            print('pilihan tidak ada')
            input('press enter to continue')
            os.system('cls')
        self.list_baru1.append(self.nama_sayur)
        self.list_baru2.append(self.jumlah_item)
        self.listbeli1 = sum(self.list_baru1)
        self.listbeli2 = sum(self.list_baru2)
        self.mau_nambah()

    def mau_nambah(self):
        x = input('apakah mau nambah Y/N ')
        x = x.lower()
        if x == 'y':
            self.template1()
        else:
            os.system('cls')
            self.template3()


if __name__ == '__main__':
    list_baru1 = []
    list_baru2 = []
    total = 0
    nama_sayur = ['Bayam', 'Wortel', 'Tomat', 'Terong']
    harga_sayur = [5000, 6000, 3500, 9000]
    list_kode = ['013', '015', '017']
    print('masukkan nama')
    nama = input()
    os.system('cls')
    lu = supermarket(nama, list_kode, nama_sayur, harga_sayur,
                     total, list_baru1, list_baru2)
    l = lu.menu()

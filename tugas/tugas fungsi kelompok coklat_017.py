# COKLAT
# Rizky Yanuar K(22031554017)
# Ilham Warmandev(22031554049)
# Aldora Novrizal Nitimanta(22031554033)
# Joevita Salsabila Fitrianova(22031554031)
# Dian ayu fauziah(22031554011)
# Pinjam Buku Perpus
# ===================================================================================================
import os
from tkinter import Menu


class library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def loginpage(self):
        os.system('cls')
        print("Selamat Datang di Perpustakaan")
        print("Enter your choice to continue")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            os.system('cls')

            self.login()
        elif choice == 2:
            os.system('cls')

            self.register()
        elif choice == 3:
            exit()

        else:
            print("Not a valid option")
            input("Press enter to continue")
            self.loginpage()

    def login(self):
        print("Masukkan nama anda: ")
        name = input()
        print("Masukkan password anda: ")
        password = input()
        self.name = name
        self.menu()

    def register(self):
        print("Masukkan nama anda: ")
        name = input()
        print("Masukkan password anda: ")
        password = input()
        print("Masukkan alamat anda: ")
        address = input()
        print("masukkan umur anda: ")
        age = input()

        print("Registration Successful")
        input("Press enter to continue")
        self.loginpage()

    def menu(self):
        os.system('cls')

        print(f"Selamat Datang di Perpustakaan {self.name}")

        print("Masukkan pilihan anda untuk melanjutkan")
        print("1. Daftar buku")
        print("2. Meminjam buku")
        print("3. Tambahkan buku")
        print("4. Mengembalikan buku")
        print("5. Exit")
        choice = int(input())
        if choice == 1:
            os.system('cls')

            self.displayBook()
        elif choice == 2:
            os.system('cls')

            book = input("Masukkan nama buku yang ingin anda pinjam: ")
            huruf_kecil = book.lower()

            if huruf_kecil not in self.booklist:
                print("Book not found")
                input("Press enter to continue")
                self.menu()
            else:
                user = self.name
                self.lendBook(user, book)

        elif choice == 3:
            os.system('cls')

            book = input("Masukkan nama buku yang ingin Anda tambahkan: ")
            self.addBook(book)
        elif choice == 4:
            os.system('cls')

            book = input("Masukkan nama buku yang ingin dikembalikan: ")
            self.returnBook(book)
        elif choice == 5:
            os.system('cls')
            exit()
        else:
            print("Not a valid option")
            input("Press enter to continue")
            self.menu()

    def addBook(self, book):
        self.booklist.append(book)
        print("Buku telah ditambahkan ke daftar buku")

        input("Press enter to continue")
        self.menu()

    def displayBook(self):
        print(f"Kami memiliki buku berikut di perpustakaan kami {self.name} :")
        for book in self.booklist:
            print(book)

        input("Press enter to continue")
        self.menu()

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print(
                "Data buku pemberi pinjaman telah diperbarui. Kamu bisa ambil bukunya sekarang")
        else:
            print(f"Buku sudah digunakan oleh {self.lendDict[book]}")

        input("Press enter to continue")
        self.menu()

    def returnBook(self, book):
        self.lendDict.pop(book)
        print("Buku telah dikembalikan")

        input("Press enter to continue")
        self.menu()


if __name__ == "__main__":
    list = ['biografi', 'ensiklopedia',
            'novel', 'cergam', 'komik',
            'buku ilmiah', 'tafsir',
            'kamus', 'buku panduan',
            'majalah', 'fotografi']
    name = ''
    lib = library(list, name)

    lib.loginpage()

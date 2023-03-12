class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def cekPinAwal(self):
        return self.defaultPin

    def cekSaldoAwal(self):
        return self.defaultBalance

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 25000000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkId(self):
        return self.id
    def checkPin(self):
        return self.pin
    def checkBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal

import random
import datetime

atm = Customer(id)

while True:

    id = int(input("Pin mu berapa : "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin salah, jangan ngarang deh : "))
        trial += 1

        if trial == 3:
            print("Error. haduhhh bisa ga sih")
            exit()

    while True:
        print("Selamat Datang di Bank Sains Data")
        print("\n 1 - Cek Saldo \n 2 - Tarik Tunai \n 3 - Setor Tunai \n 4 - Ganti Pin \n 5 - Keluar ")

        selectmenu = int(input("\nMau yang mana hayoo : "))

        if selectmenu == 1:
            print("\nSisa saldomu miris sekali, ayo diisi lagi : Rp." + str(atm.checkBalance()) + "\n")

        elif selectmenu == 2:
                nominal = float(input("Berapa ini : "))
                verify_withdraw = input("Yakin segini???" +" "+str(nominal) + "? y/n" +" ")
                if verify_withdraw == "y":
                    print("Saldomu tadi : Rp. " + str(atm.checkBalance()) + " ")
                else:
                    break
                if nominal < atm.checkBalance():
                    atm.withdrawBalance(nominal)
                    print("Berhasil wahh ngeriii")
                    print("Sisa saldomu hmm : Rp. " + str(atm.checkBalance()) + "")
                else:
                    print("Sorry yaa, saldomu ga cukup isi dulu gihh")
                    print("Sok tambahin saldonya")

        elif selectmenu == 3:
                nominal = float(input("Mau berapa ini :"))
                verify_deposit = input("Udah gini doang? simpan nihh"+" "+ str(nominal) + "? y/n" +" ")
                if verify_deposit == "y":
                    atm.depositBalance(nominal)
                    print("Sisa segini saldomu : Rp." + str(atm.checkBalance()) + "\n")
                else:
                    break

        elif selectmenu == 4:
            verify_pin = int(input("Pinmu berapa : "))
            while verify_pin != int(atm.checkPin()):
                print("Pin salah, jangan ngarang :")
                break
            
            update_pin = int(input("jadi mau berpa ini?? :"))
            print("wihh berhasil ngeriii")
            verify_newpin = int(input("coba lagi deh : "))
            
            if verify_newpin == update_pin:
                print("wihh berhasil ngeriii!")
            else:
                print("Pin salah, jangan ngarang ")

        elif selectmenu == 5:
            print("========================================")
            print("Resi tercetak otomatis saat anda keluar.\n")
            print("Harap simpan tanda terima ini \n")
            print("sebagai bukti transaksi anda.")
            print("\nNo. Rekord:", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo Akhir: ", atm.checkBalance())
            print("\nTerima kasih telah menggunakan BANK SAINS DATA")
            print("========================================")
            exit()

        else:
            print("Error. Maaf menu anda tidak tersedia")
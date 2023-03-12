# COKLAT
# Rizky Yanuar K(22031554017)
# Ilham Warmandev(22031554049)
# Aldora Novrizal Nitimanta(22031554033)
# Joevita Salsabila Fitrianova(22031554031)
# Dian ayu fauziah(22031554011)
# Pinjam Buku Perpus
# ===================================================================================================


print("""Peraturan meminjam buku:
1) Jumlah buku yang dapat dipinjam maks. 2 buku dengan periode peminjaman selama 7 hari.
2) Keterlambatan pengembalian buku dikenakan denda.
3) Apabila terjadi kehilangan buku, peminjam harus mengganti dengan buku yang sesuai.""")
print("========================================================================================")


def Data_Peminjam():
    print("Masukkan Data Berikut:")
    a = input("Nama \t\t: ")
    b = input("NIM \t\t: ")
    c = int(input("Tanggal peminjaman buku : "))
    d = c+7
    if d > 31:
        print("Kembalikan buku anda pada tanggal", [c-24], "bulan depan!")
    else:
        print("Kembalikan buku pada tanggal", c+7)
    print("Deadline pengembalian buku anda adalah satu minggu dari sekarang", )
    print("Jika anda terlambat mengembalikan buku, anda terkena sanksi sebesar: Rp.5000")
    return


Data_Peminjam()


def pilih_buku():
    menu = 1
    print("Buku yang ingin dipinjam: ")
    pilihan1 = input('Masukkan Judul Buku \t: ')
    kodebuku1 = input('Kode Buku \t\t: ')
    tambah = input('Tambah Buku (Y/N) \t: ')
    if tambah == 'Y':
        pilihan2 = input('Judul Buku Kedua \t: ')
        kodebuku2 = input('Kode Buku \t\t: ')
        menu += 1
        print("==============================================")
        print(f"Judul buku 1\t:{pilihan1}")
        print(f"Kode Buku\t:{kodebuku1}")
        print(f"Judul buku 2\t:{pilihan2}")
        print(f"Kode Buku\t:{kodebuku2}")
        print('Terima kasih, Jangan lupa kembalikan buku sesuai deadline yang diberikan!')
        print("==============================================")
        return [pilihan1, pilihan2]
    else:
        print("==============================================")
        print(f"Judul Buku\t: {pilihan1}")
        print(f"Kode Buku\t: {kodebuku1}")
        print('''Terima kasih, Jangan lupa kembalikan buku
sesuai deadline yang diberikan!''')
        return [pilihan1]
        print("==============================================")


pilihan_buku = pilih_buku()


def pengembalian_buku():
    print("masukkan kode buku untuk mengetahui letak buku")
    e = input("Kode Buku \t: ")
    x = int(e)
    max_data = 2000
    while x >= (max_data + 1):
        print("Kode buku tidak ditemukan")
        x = int(input("Kode Buku \t: "))
    else:
        if x % 2 == 1:
            print("kembalikan buku di rak nomor 1-10")
        else:
            print("kembalikan buku di rak nomor 11-20")
    print("==============================================")
    x = int(input("Tanggal peminjaman buku\t\t: "))
    y = int(input("Tanggal pengembalian buku\t: "))
    z = x+7
    if y > z:
        print('''Anda terlambat mengembalikan buku dan terkena sanksi sebesar Rp. 5000,
Jangan lupa kembalikan buku sesuai tempat yang diinstruksikan''')
    else:
        print('''Terima Kasih telah mengembalikan buku,
Mohon kembalikan buku sesuai tempat yang diinstruksikan :)''')

    return


pengembalian_buku()

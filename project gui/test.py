# import struct
# fmt = "<12s i f"
# book = struct. Struct(fmt)
# with open("books.bin", "wb") as binary_file:
#     binary_file. write(book.pack(b"book bindo", 123, 45.67))
# with open("books.bin", "rb") as binary_file:
#     data = binary_file.read(book.size)
#     values = book.unpack(data)
# # menampilkan hasil unpack
#     print(values)
# packed = struct.pack('!is', 1, 'kiki')
# unpacked = struct.unpack('!is', packed)
# print(packed)
# print(unpacked)

# import array as arr
# import struct
# import os

# mahasiswa_struct = struct.Struct("30s 30s i f")
# with open("mahasiswa.bin", "wb") as f:
#     mahasiswa1 = (b"Mahesa Fiko", b"Computer Science", 123456789, 3.5)
#     f.write(mahasiswa_struct.pack(*mahasiswa1))
#     mahasiswa2 = (b'Dian Ayu', b"Data", 987654321, 3.7)
#     f.write(mahasiswa_struct.pack(*mahasiswa2))

# with open("mahasiswa.bin", "rb") as f:
#     while True:
#         data = f.read(mahasiswa_struct.size)
#         if not data:
#             break
#         mahasiswa = mahasiswa_struct.unpack(data)
#         print("Nama:", mahasiswa[0].decode().strip(), "\nProdi:",
#               mahasiswa[1].decode().strip(), "\nNlM:", mahasiswa[2], '\nIPK:', mahasiswa[3])

# with open('mahasiswa bin', 'ab') as f:
#     nama = input('masukan nama:')
#     nama = nama.encode('utf-8')
#     prodi = input('masukkan prodi:')
#     prodi = prodi.encode('utf-8')
#     nim = int(input('masukkan nim:'))
#     ipk = float(input('masukkan ipk:'))
#     os.system('cls')
#     mahasiswabaru = (nama, prodi, nim, ipk)
#     f.write(mahasiswa_struct.pack(*mahasiswabaru))

# with open("mahasiswa.bin", "rb") as f:
#     while True:
#         data = f.read(mahasiswa_struct.size)
#         if not data:
#             break
#         mahasiswa = mahasiswa_struct.unpack(data)
#         print("Nama:", mahasiswa[0].decode().strip(), "\nProdi:",
#               mahasiswa[1].decode().strip(), "\nNlM:", mahasiswa[2], '\nIPK:', mahasiswa[3])
import os


class Participant:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


puskesmas = Stack()
while True:
    print("1. tambah data")
    print("2. print data")
    print("3. keluar")

    inputan = int(input(''))
    os.system('cls')

    if inputan == 1:
        name = input("Masukan nama pasien: ")
        age = int(input("Masukan umur pasien: "))

        if age >= 50:
            partisipan = Participant(name, age)
            puskesmas.push(partisipan)
            os.system('cls')
            print(f"{name} sudah di tambahkan")

        else:
            os.system('cls')
            print(
                f"{name} Umur harus di atas 50")

    elif inputan == 2:
        os.system('cls')

        sorted_participants = sorted(
            puskesmas.items, key=lambda x: x.age, reverse=True)

        for partisipan in sorted_participants:
            print(f"nama: {partisipan.name}, umur: {partisipan.age}")

    else:
        os.system('cls')
        break

"""Nomor 1"""

import os


# class stacke:
#     def __init__(self, max):
#         self.list = []
#         self.size = 0
#         self.size_max = max

#     def __str__(self):
#         values = [str(x) for x in self.list]  # mengubah tipe data menjadi str
#         return ' '.join(values)

#     def isempty(self):
#         if self.list == []:
#             return True
#         else:
#             return False

#     def push(self, value):
#         if self.size < self.size_max:
#             self.list.append(value)
#             self.size += 1
#         else:
#             print("stacknya full")

#     def pop(self):
#         if self.isEmpty():
#             return "Stack kosong"
#         else:
#             self.size -= 1
#             return self.list.pop()

#     def isFull(self):
#         if self.list == self.size_max:
#             return True
#         else:
#             return False


# sstack = stacke(10)
# sstack.push(1)
# sstack.push(2)
# sstack.push(3)
# sstack.push(4)
# sstack.push(5)
# sstack.push(6)
# sstack.push("naspad")
# sstack.push(8000)
# sstack.push(9500)
# sstack.push("bakso")
# sstack.push(11)

# sstack.size
# print(sstack)
# sstack.isFull()


# """Nomor 2"""


# class stack:
#     def __init__(self):
#         self.items = []
#         self.minimalitem = None

#     def push(self, item):
#         self.items.append(item)
#         if self.minimalitem is None or item < self.minimalitem:
#             self.minimalitem = item

#     def pop(self):
#         if not self.is_empty():
#             item = self.items.pop()
#             if item == self.minimalitem:
#                 self.minimalitem = min(
#                     self.items) if not self.is_empty() else None
#             return item

#     def is_empty(self):
#         return len(self.items) == 0

#     def minimailitem(self):
#         return self.minimalitem


# stack = stack()
# stack.push(15700)
# stack.push(2000)
# stack.push(5000)
# stack.push(1900)
# print(stack.minimailitem())  # Output: 1
# stack.pop()
# stack.pop()
# print(stack.minimailitem())  # Output: 3


"""nomer 3"""


# class Participant:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return not bool(self.items)

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)


# puskesmas = Stack()
# while True:
#     print("1. tambah data")
#     print("2. print data")
#     print("3. keluar")

#     inputan = int(input(''))
#     os.system('cls')

#     if inputan == 1:
#         name = input("Masukan nama pasien: ")
#         age = int(input("Masukan umur pasien: "))

#         if age >= 50:
#             partisipan = Participant(name, age)
#             puskesmas.push(partisipan)
#             os.system('cls')
#             print(f"{name} sudah di tambahkan")

#         else:
#             os.system('cls')
#             print(
#                 f"{name} Umur harus di atas 50")

#     elif inputan == 2:
#         os.system('cls')

#         sorted_participants = sorted(
#             puskesmas.items, key=lambda x: x.age, reverse=True)

#         for partisipan in sorted_participants:
#             print(f"nama: {partisipan.name}, umur: {partisipan.age}")

#     else:
#         os.system('cls')
#         break


# class Lansia:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

# class Antrian:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return self.items == []

#     def enqueue(self, item):
#         # find the index to insert the new item based on age
#         index = 0
#         for i in range(len(self.items)):
#             if item.usia > self.items[i].usia:
#                 index = i + 1
#             else:
#                 break
#         self.items.insert(index, item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)


# # Data peserta lansia yang sudah diketahui
# data_peserta = [
#     Lansia("stevenko", 52),
#     Lansia("Budidoremi", 60),
#     Lansia("megaa", 45),
#     Lansia("Jokowi", 55),
#     Lansia("puan", 70),
#     Lansia("Dewangga", 63)
# ]

# # Membuat antrian peserta yang memenuhi syarat
# antrian = Antrian()
# for peserta in data_peserta:
#     if peserta.usia >= 50:
#         antrian.enqueue(peserta)

# # Memproses peserta dalam antrian
# while not antrian.is_empty():
#     peserta = antrian.dequeue()
#     print("Peserta dengan nama", peserta.nama,
#           "dan usia", peserta.usia, "telah dilayani.")

# def countdown(n):
#     for i in range(n, -1, -1):
#         if i <= 0:
#             print('blastoff')
#         else:
#             print(i)
# countdown(3)

# def mult_iter(a, b):
#     result = 0
#     while b > 0:
#         result += a
#         b -= 1
#     return result


# a = 5
# b = 6
# result = mult_iter(a, b)
# print(result)

def factorial_rekursif(n):
    if (n == 1) or (n == 0):
        return 1
    else:
        return n*factorial_rekursif(n-1)


print(factorial_rekursif(100))

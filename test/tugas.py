# nama = input('masukkan nama :')
# no = int(input('masukkan no :'))

# if no > 0:
#     print(f'{no} = Positif')
# else:
#     print(f'{no} = Negatif')


# nama = input('masukkan nama :')
# no = int(input('masukkan no :'))

# if no > 0:
#     print(f'{no} = Positif')
# else:
#     print(abs(no))

# my_var = int(input('masukkan angka :'))
# if (my_var % 2) == 0:
#     if (my_var**3 != 27):
#         my_var = my_var + 4
#     else:
#         my_var /= 1.5
# else:
#     if my_var <= 10:
#         my_var *= 2
#     else:
#         my_var *= 2
# print(my_var)


# n = int(input('masukkan angka :'))
# if (n % 2) == 0:
#     print(f'ini bilangan genap = {n}')
# elif n == 0:
#     print(f'ini bilangan nol = {n}')
# else:
# print(f'ini bilangan ganjil = {n}')

# i = 1
# while i < 6:
#     print(i)
#     i += 2

# y = int(input('masukkan angka :'))
# while y != 2:
#     print(y)
#     y = int(input('masukkan angka :'))

# n = int(input('masuakan angka:'))
# while (n % 2) != 0:
#     print("Ganjil")
#     n = int(input('masukan Angka lagi'))
# else:
#     print('genap')

# n = int(input('masukan angka:'))
# sum = 0
# while n > 0:
#     sum += n
#     n -= 1
# print(sum)

# adj = ['red', 'big', 'tasty']
# fruits = ['apple', 'banana', 'cherry']

# for y in adj:
#     for y in fruits:
#         print(y, y)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i*j, end="")
#     print()

# number_str = input("Enter an int:")
# number = int(number_str)
# count = 0
# while number > 9:
#     if number % 2 == 0:
#         number = number // 2
#     elif number % 3 == 0:
#         number = number // 3
#     else:
#         number = number - 1
#     count = count + 1
# print("Count is: ", count)
# print("Number is: ", number)


# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1


# y = int(input("Masukkan angka: "))
# for i in range(1, y+1):
#     for y in range(1, i+1):
#         print(y, end=" ")
#     print("")


# number = [12, 75, 150, 180, 145, 525, 50]
# for i in number:
#     if i % 5 == 0:
#         if i > 500:
#             break
#         elif i > 150:
#             continue
#         print(i)


# y = int(input("Masukkan angka: "))
# for i in range(y, 0, -1):
#     for j in range(y, 0, -1):
#         print(j, sep='-', end=' ')
#     y -= 1
#     print('')


# from itertools import count


# x = int(input('masukkan angka: '))
# for i in range(1, x+1):
#     for y in range(1, i+1):
#         print(y, end='')
#     print()

# x = int(input('masukkan angka:'))
# for i in range():
#     print(i)


# s = 'jago coding'
# print(s[0])
# print(s[4])
# print(s[-3])
# print(len(s))
# print(s[len(s)-1])

# kalimat = 'unesa satu langkah di depan '
# print('nesa' in kalimat)
# print('tulang' in kalimat)
# print('tu lang' in kalimat)

# kalimat = 'fmipa selalu di depan'
# for char_idx in range(len(kalimat)):
#     print(kalimat[char_idx])


# kalimat = 'fmipa selalu di depan'
# char_idx = len(kalimat) - 1
# while char_idx >= 0:
#     print(kalimat[char_idx], end="")
#     char_idx -= 1

# kalimat = 'pemrograman dasar'
# target = input('masukkan karakter: ')
# for index in range(len(kalimat)):
#     if kalimat[index] == target:
#         print('kata ditemukan', index)
#         break
#     else:
#         print('kata', target, "tidak ditemukan di", kalimat)

# kalimat = 'pemrograman dasar'
# x = input('masukkan huruf: ')
# print(f'kalimat ditemukan di index {kalimat.find(x)}')

# kalimat = 'aku pasti bisa mendapat nilai A untuk mata kuliah Pemrograman dasar'
# var = kalimat.split(" ")
# for i in var:
#     print(i)

# nama = input('masukkan nama lengkap: ')
# nim = input('masukkan nim: ')
# var = nama.split(" ")
# nama_depan = var[0]
# nama_belakang = var[-1]
# # print(f'Nama depan: {nama_depan}')
# # print(f'Nama belakang: {nama_belakang}')
# dpn_nim = nim[0:4]
# nim_ab = nim[-4:]
# # print(f'Angkatan: {dpn_nim}')
# print(f'nama panjang\t:{nama}')
# print(f'nama depan\t:{nama_depan}')
# print(f'nama belakang\t:{nama_belakang}')
# print(f'NIM\t\t:{nim}')
# print(f'Tahun Angkatan\t:{dpn_nim}')
# if int(nim_ab) % 2 == 0:
#     print(f'Kelas\t\t:2022A')
# else:
#     print(f'Kelas\t\t:2022B')

# from unittest import result
# print(nim_ab)

# def my_factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= 1
#     return result


# print(my_factorial(4))


# def pengembalian_buku():
#     e = int(input("Kode Buku: "))
#     max_data = 1000
#     while e >= max_data:
#         print("Kode buku tidak ditemukan :( ")
#         e = int(input("Kode Buku: "))
#     else:
#         if e <= max_data:
#             if e % 2 == 1:
#                 print("kembalikan buku di rak nomor 1-10")
#             else:
#                 print("kembalikan buku di rak nomor 11-20")


# # pengembalian_buku()

# def pengembalian_buku():
#     e = input("Kode Buku: ")
#     x = int(e)
#     max_data = 2000
#     while x >= max_data:
#         print("Kode buku tidak ditemukan :( ")
#         e = int(input("Kode Buku: "))
#     else:
#         if x % 2 == 1:
#             print("kembalikan buku di rak nomor 1-10")
#         else:
#             print("kembalikan buku di rak nomor 11-20")


# pengembalian_buku()

# kata = '#2022GoalsComeTrue!!'
# huruf = 0
# angka = 0
# simbol = 0

# for i in kata:
#     if i.isalpha() == True:
#         huruf += 1
#     elif i.isdigit() == True:
#         angka += 1
#     else:
#         simbol += 1


# print(f'huruf={huruf}')
# print(f'angka={angka}')
# print(f'simbol={simbol}')

# s1 = {1,2,5}
# s2 = {2,3}
# print(s1 - s2)
# print(s1 ^ s2)

# List_angka = [2, 2, 3, 4, 12, 5, 2, 5, 7, 3,
#               10, 11, 2, 1, 3, 5, 4, 6, 12, 0, 1, 2]
# x = int(input('masukkan angka'))
# while List_angka == x:
#     y = List_angka.remove(x)
#     print(y)

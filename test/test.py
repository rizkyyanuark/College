
# Variable = ""
# baris = 1
# inputan = int(input("Mau berapa baris:"))
# while baris <= inputan:
#     kolom = baris
#     while kolom > 0:
#         Variable = Variable + " [] "
#         kolom = kolom - 1
#     Variable = Variable + "\n"
#     baris = baris + 1
# print(Variable)


# x = 3
# y = 7
# z = 5
# data = (x*(z+y))
# print(f"{x} * ( {z} + {y} )")


# angka = [0, 1, 2, 3, 4, 5]
# for i in angka:
#     print(f"ini nilainya : {i}")

# print("buat makalah mengenai memory word and ppt")

# string = ""
# bar = 1
# input = int(input('masukan baris'))
# while baris <= inputan:
# 	kolom = bar
# 	while kolom > 0:
# 		string = string + '[]'
# 		kolom = kolom -1

# def selamat_datang():
#     x = input('masukkan nim: ')
#     y = ''
#     nimdef = '22031554'
#     while len(x) != 3:
#         print("harus 3 digit!")
#         x = input('masukkan ulang: ')
#     else:
#         z = (nimdef + x) + y
#         print(z)
# selamat_datang()


from turtle import width


# class houses():
#     def __init__(self, owner, collor,):
#         self.owner = owner
#         self.collor = collor


# inputowner = input("masukan nama: ")
# inputcollor = input("masukan warna rumah: ")
# house1 = houses(inputowner, inputcollor)
# print(house1.owner)
# print(house1.collor)


# class cube():
#     def __init__(self, length, width, tall):
#         self.length = length
#         self.width = width
#         self.tall = tall

#     def get_volume(self):
#         vol = self.length*self.width*self.tall
#         return vol


# inputlength = input("masukan panjang: ")
# inputwidth = input("masukan lebar: ")
# inputtall = input("masukan tinggi: ")

# cube1 = cube(inputlength, inputwidth, inputtall)

# for x in [1,2,3,4]:
#     print (x)
# for x in range [1,5]:
#     print (x)

# n=input("masukkan angka:")
# n = int(n)
# sum = 0  
# for i in range(n+1):
#     sum += i   
# print (sum)

# n=input("masukkan angka:")
# n = int(n)
# sum = 1  
# for i in range(0, n+1, 2):
#     sum += i   
# print (sum)

# matakuliah = ["kalkulus", "pemrograman", "statistika", "arsitektur komputer", "bahasa indonesia", "bahasa inggris", "agama", "pancasila", "olahraga"]
# for x in range(1,9,2):
#     print (matakuliah [x]) 

# x = int(input ("masukkan angka:"))
# for x in range(2,21,2):
#     print (x)

# list = [10, 20, 30, 40, 50]
# for x in range(4, 0,-1):
#     print (list [x])

# i = 10
# while i >3: 
#     print(i)
#     i-= 1

# n = int(input("masukkan angka:"))
# while (n%2 !=0):
#     print ("ganjil")
#     n = int(input("masukkan angka:"))

# n=input("masukkan angka:")
# n = int(n)
# sum = 0
# while n >0:
#     sum += n 
#     n-= 1
#     print (sum)

# import os
# from secrets import choice
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for i in range(2,5):
#     for j in range(4,7):
#         print(i*j, end='')
#         print()

# number_str = input("enter an int:")
# number = int(number_str)
# count =0
# while number >0:
#     if number %2 ==0:
#         number = number// 2
#     elif number %3 == 0:
#         number = number //3
#     else: 
#         number = number - 1 
#     count = count + 1 
# print("count is: ", count)
# print("number is: ", number)

# fruits = ["apple","banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# import math


# class trianggle():
#     def __init__(self, x1, x2, x3, y1, y2, y3):
#         self.x1 = x1
#         self.x2 = x2
#         self.x3 = x3
#         self.y1 = y1
#         self.y2 = y2
#         self.y3 = y3

#     def calculate_area(self):
#         def side_length(x1, x2, y1, y2):
#             math = ((x1-x2)**2 + (y1-y2)**2)
#             return math
#         a = side_length(self.x1, self.y1, self.x2, self.y2)
#         b = side_length(self.x2, self.y2, self.x3, self.y3)
#         c = side_length(self.x3, self.y3, self.x1, self.y1)
#         s = (1/2)*(a + b + c)
#         mat = (s*(s-a)*(s-b)*(s-c))
#         return mat


# x1 = int(input('masukkan x1: '))
# x2 = int(input('masukkan x2: '))
# x3 = int(input('masukkan x3: '))
# y1 = int(input('masukkan y1: '))
# y2 = int(input('masukkan y2: '))
# y3 = int(input('masukkan y3: '))

# seg = trianggle(x1, x2, x3, y1, y2, y3)
# print(seg.calculate_area())

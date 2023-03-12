# adj=["red","big","tasty"]
# fruits=["apple","banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# count=0
# while(count<9):
#     print("the count is:",count)
#     count=count+1
# print("good bye!")

# matakuliah=["kalkulus","pemograman","statistika"]
# for favorit in matakuliah:
#     print("saya suka kuliah",favorit)

# num = 1
# while True:
#     print(num)
#     num += 1
#     if num >= 4:
#         break

# for i in range(15):
#     if i % 2 ==1:
#         continue
#     print(i)

# matakuliah=["kalkulus","pemograman","statistika"]
# nilai=["80","85"]
# for favorit in matakuliah:
#     for nilai2 in nilai:
#         print("nilai mata kuliah",favorit,"saya adalah", nilai2)

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end=' ')
#     print()

# rows=5
# #outer loop
# for i in range(1, rows+1):
#     #inner loop
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print('')


# for i in range(1, 10):
#     if (i % 2 == 0 and i != 10):
#         if i in [6, 4]:
#             continue
#         else:
#             print(i)


# n = int(input('masukkan nilai n:'))
# faktorial = 5
# for i in range(1, n+1):
#     faktorial *= i
#     print(f'{n}\t:{faktorial}')


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

# list_sayur = {'Bayam': 5000, 'Wortel': 3500, 'Tomat': 6000,
#               'Terong': 9000}
# nama_sayur = list_sayur.keys()
# harga_sayur = list_sayur.values()
# for key in list_sayur.keys():
#     print(key)
# print()
# for key1 in list_sayur.values():
#     print(key1)
# print()

# print(f'{key}={key1}')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary*4


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked*self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return (self.weekly_salary)*4


class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


salary_employee = SalaryEmployee(1, 'paiz', 900)
hourly_employee = HourlyEmployee(2, 'riba', 35000, 100)
commission_employee = CommissionEmployee(3, 'rijeki', 1000000, 2000000)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee, hourly_employee, commission_employee])

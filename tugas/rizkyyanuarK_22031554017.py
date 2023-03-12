
# nomer satu
y = int(input("Masukkan angka: "))
for i in range(1, y+1):
    for y in range(1, i+1):
        print(y, end=" ")
    print("")

# nomer dua
number = [12, 75, 150, 180, 145, 525, 50]
for i in number:
    if i % 5 == 0:
        if i > 500:
            break
        elif i > 150:
            continue
        print(i)

# nomer tiga
y = int(input("Masukkan angka: "))
for i in range(y, 0, -1):
    for j in range(y, 0, -1):
        print(j, sep='-', end=' ')
    y -= 1
    print('')


s = 'jago coding'
print(s[0])

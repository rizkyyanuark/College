import pandas
from skimage import color
import matplotlib.pylab as plt
import csv

def merge_sort(arr, key=512):
    if len(arr) > 1:
        # devide
        mid = len(arr) // 2  
        left_half = arr[:mid]
        right_half = arr[mid:]

        # memanggill lagi fungsi untuk tujuan memecah lebih kecil lagi array
        merge_sort(left_half, key=key)
        merge_sort(right_half, key=key)

        # untuk menginisiasi
        i = j = k = 0

        # membandingkan sisi kiri dengan sisi kanan(merge)
        while i < len(left_half) and j < len(right_half):
            if key(left_half[i]) < key(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

with open('Data_indeks_UTSB.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) # skip header row
    data = []
    for row in reader:
        data.append(row)
    merge_sort(data, key=lambda x: int(x[0]))

with open('Hasil_Urut_Index_UTS.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for row in data:
        writer.writerow(row)
        
df = pandas.read_csv('Hasil_Urut_Index_UTS.csv')
df = df.drop(columns=['indeks'])
plt.imshow(df, cmap=plt.cm.gray, vmin=0, vmax=1)
plt.show()
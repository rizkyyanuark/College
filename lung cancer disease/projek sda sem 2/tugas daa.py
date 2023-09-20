def uanggreedy(uang, koin=[1000, 500, 200, 100], index=0):
    if index >= len(koin):
        return {}
    nilai_koin = koin[index]
    if uang >= nilai_koin:
        jumlah_koin = uang // nilai_koin
        uang -= jumlah_koin * nilai_koin
        hasil_penukaran = {nilai_koin: jumlah_koin}
    else:
        hasil_penukaran = {}
    hasil_penukaran.update(uanggreedy(uang, koin, index + 1))
    return hasil_penukaran


uang = int(input("Masukkan jumlah uang dalam Rupiah: "))
hasil = uanggreedy(uang)

print(f"Uang: {uang} \nHasil penukaran uang:")
for nilai, jumlah in hasil.items():
    print(f"{jumlah} koin x {nilai} Rupiah")

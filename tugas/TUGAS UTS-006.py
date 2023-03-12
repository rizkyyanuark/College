# tugas pertemuan 8
# 22031554006
# test
# wkwkwk
# dscfkjsd
import os

bindo_jawa = {
    "satu": "siji",
    "dua": "loro",
    "tiga": "telu",
    "empat": "papat",
    "lima": "limo/gangsal",
    "enam": "enem",
    "tujuh": "pitu",
    "delapan": "wolu",
    "sembilan": "sanga(songo)",
    "sepuluh": "sedasa",
    "sebelas": "sewelas",
    "Dua belas": "rolas",
    "Tiga belas": "telulas",
    "Empat belas": "patbelas",
    "Lima belas": "limolas",
    "Enam belas": "nembelas",
    "Tujuh belas": "pitulas",
    "Delapan belas": "wolulas",
    "Sembilan belas": "songolas",
    "Dua puluh": "rongpuluh"
}
os.system("cls")
values = bindo_jawa.values()
keys = bindo_jawa.keys()
for key in bindo_jawa.keys():
    print("KUNCI: " + key)
print()


def translatejawa(kata_indo):
    text_list = []
    for index, text in enumerate(kata_indo):
        splitline = text.split()
        for word in bindo_jawa:
            if word in bindo_jawa:
                text = text.replace(word, str(bindo_jawa[word]))
                kata_indo[index] = text
    return kata_indo


kata_indo = [input("MASUKAN KUNCI: ")]
print(translatejawa(kata_indo))

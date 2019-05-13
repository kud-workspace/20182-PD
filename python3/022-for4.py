#!/usr/bin/env python3

awal = int(input("Masukkan Nilai awal: "))
akhir = int(input("Masukkan Nilai akhir: "))
dec = int(input("Masukkan Nilai decrement: "))

for x in range (awal, akhir + 1, dec) :
    print(x)

#!/usr/bin/env python3

awal = int(input("Masukkan Nilai awal: "))
akhir = int(input("Masukkan Nilai akhir: "))
inc = int(input("Masukkan Nilai increment: "))

for x in range (awal, akhir + 1, inc) :
    print(x)

#!/usr/bin/env python3

awal = int(input("Masukkan Nilai Awal "))
akhir = int(input("Masukkan Nilai Akhir "))
incr = int(input("Masukkan Nilai increment "))

i = awal # nilai awal

while i >= akhir : # kondisional
    print(i)
    i = i - incr # increment
    #i -= 1

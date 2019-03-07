#!/usr/bin/env python3

awal = int(input("Masukkan Nilai Awal "))
akhir = int(input("Masukkan Nilai Akhir "))
inc = int(input("Masukkan Nilai increment "))

i = awal # nilai awal
total = 0

while i <= akhir : # kondisional
    print(i, end=' ')
    if i != akhir :
        print("+", end=' ')
    total = total + i
    i = i + inc # increment
    #i += 1

print("=", total)

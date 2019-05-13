#!/usr/bin/env python3

def tambah(a, b): # procedure
    x = a + b
    print("%d + %d = %d" %(a, b, x))

def kali(a, b): # function
    x = a * b
    return x

def pangkat(a, b):
    total = 1
    i = 0
    while i < b:
        total = total * a
        i = i + 1
    return total

a = 0
b = 0

pilih = 0
while pilih != 3:
    print("1. Masukan Data\n2. perhitungan\n3. Keluar")
    pilih = int(input("Masukan pilihan anda "))

    if pilih == 1:
        a = int(input("Masukkan variabel a "))
        b = int(input("Masukkan variabel b "))

    elif pilih == 2:
        print("%d pangkat %d = %d" %(a, b, pangkat(a, b)))

    print()

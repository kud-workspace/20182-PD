#!/usr/bin/env python3

harga = 1500
print("Harga komputer -> Rp", harga, "(dalam ribuan)")

jumlah = int(input("Masukan jumlah barang "))
print("harga normal ->", jumlah, "x Rp", harga, "= Rp", jumlah * harga)

diskon = 0.1
jumlah_diskon = jumlah * harga * 0.1
print("harga discount 10% ->", "(%d x Rp %d) - (%d x Rp %d x %1.1f) = Rp %d" %(jumlah, harga, jumlah, harga, diskon, jumlah * harga - jumlah_diskon))

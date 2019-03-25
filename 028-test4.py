#!/usr/bin/env python3

# while
print("""1. buku   harga Rp 1000/buah
2. pinsil harga Rp 1500/buah
beli buku lebih dari 10 dapat discount 10% dan pinsil 5%""")
pilihan1 = int(input("Masukan pilihan anda "))

if pilihan1 == 1:
    harga = 1000
    diskon = 0.1

elif pilihan1 == 2:
    harga = 1500
    diskon = 0.05

pilihan2 = int(input("Masukan increment -> 1 (for)dan decrement -> 2 (while) : "))
print("jumlah barang       total bayar")

if pilihan2 == 1:
    for jumlah in range (0, 21, 2):
        if jumlah == 10:
            print("%d buah           (%d buah x Rp %d)" %(jumlah, jumlah, harga), end = '')
        else:
            print("%d buah          (%d buah x Rp %d)" %(jumlah, jumlah, harga), end = '')

        if jumlah > 10:
            potongan = jumlah * harga * diskon
            print("-(%d buah x Rp %d x %1.2f) = Rp %d" %(jumlah, harga, diskon, jumlah * harga - potongan))
        else:
            print(" = Rp %d " %(jumlah * harga), "---> tidak kena discount")

elif pilihan2 == 2:
    jumlah = 100
    while jumlah >= 0:
        if jumlah == 10:
            print("%d buah           (%d buah x Rp %d)" %(jumlah, jumlah, harga), end = '')
        else:
            print("%d buah          (%d buah x Rp %d)" %(jumlah, jumlah, harga), end = '')

        if jumlah > 10:
            potongan = jumlah * harga * diskon
            print("-(%d buah x Rp %d x %1.2f) = Rp %d" %(jumlah, harga, diskon, jumlah * harga - potongan))
        else:
            print(" = Rp %d " %(jumlah * harga), "---> tidak kena discount")

        jumlah -= 2

#!/usr/bin/env python3

import os

print("Selamat datang!\n1. Memulai per-loopingan\n2. Keluar\n")
cho = int(input("Masukkan pilihan: "))

if cho == 1:
    awal = 1
    akhir = 10

    print("Metode per-loopingan:\n1. ASCENDING\n2. DESCENDING\n")
    cho = int(input("Masukkan pilihan: "))

    if (cho == 1 or cho == 2):
        os.system('clear')
        total = 0 # no-op

        if cho == 1:
            print("pilihan ASCENDING masukan 10 data")
            while awal <= akhir:
                nilai = int(input("masukan data ke %d " %(awal)))
                total = total + nilai
                awal += 1 # increment

            print("total data yang dimasukan %d" %(total))

        elif cho == 2:
            print("pilihan DESCENDING masukan 10 data")
            while akhir >= awal:
                nilai = int(input("masukan data ke %d " %(akhir)))
                total = total + nilai
                akhir -= 1 # decrement

            print("rata-rata data yang dimasukan %d" %(total / 10))

    else:
        raise Exception("Expected 1 or 2, got: %d" %(cho))

elif cho == 2:
    print("\nMengakhiri program.")
    quit() # exit

else:
    raise ValueError("Silahkan pilih 1 atau 2 bukan dirinya :'(")


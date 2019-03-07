#!/usr/bin/env python3

print("Menu\n1. Kondisi IF\n2. Keluar")
cho = int(input("Masukan pilihan anda "))

if cho == 1:
    a = int(input("Masukan nilai a "))
    b = int(input("Masukan nilai b "))
    c = int(input("Masukan nilai c "))
    jumlah = (a + b) * c

    print("(%d + %d) x %d = %d" %(a, b, c, jumlah))

    if (jumlah % 2) == 0:
        print("Total %d adalah bilangan genap" %(jumlah))
    else:
        print("Total %d adalah bilangan ganjil" %(jumlah))

    if jumlah < 10:
        print("Total %d adalah satuan" %(jumlah))
    elif jumlah < 100:
        print("Total %d adalah puluhan" %(jumlah))
    elif jumlah < 1000:
        print("Total %d adalah ratusan" %(jumlah))
#    else:
#        print("Total %d adalah ribuan" %(jumlah))

elif cho == 2:
    quit(0)

else:
    quit(1)

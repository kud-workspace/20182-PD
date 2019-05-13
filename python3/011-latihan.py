#!/usr/bin/env python3

a = int(input("Masukkan nilai a "))
b = int(input("Masukkan nilai b "))
c = int(input("Masukkan nilai c "))

print("1. Rumus (a + b) x (a + c)")
print("2. Rumus (a + b) x c")
print("3. Rumus (a + b x c)")

cho = int(input("Masukkann pilihan anda "))
if (cho == 1) :
    print("Anda Menggunakan Rumus (a+b)*(a+c)")
    print("(a + b) * (a + c) =", (a + b) * (a + c))
elif (cho == 2) :
    print("Anda Menggunakan Rumus (a+b)* c")
    print("(a + b) * c =", (a + b) * c)
elif (cho == 3) :
    print("Anda Menggunakan Rumus (a + b * c)")
    print("(a + b * c) =", (a + b * c))

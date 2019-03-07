#!/usr/bin/env python3

x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))

a = x + y
b = x - y
c = x * y
d = x / y

print("Hasil %d + %d adalah %d" %(x, y, a), end=", ")
print("Hasil", int(x), "-", int(y), "adalah", int(b))
print("Hasil kali adalah", c)
print("Hasil bagi adalah", d)

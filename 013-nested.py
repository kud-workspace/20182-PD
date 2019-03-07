#!/usr/bin/env python3

a = int(input("Masukkan nilai a "))
b = int(input("Masukkan nilai b "))
c = int(input("Masukkan nilai c "))

if (a < b and a < c) :
    if (b < c) :
       print("%d %d %d" %(a, b, c))
    else :
       print("%d %d %d" %(a, c, b))
elif (b < a and b < c) :
    if (a < c) :
       print("%d %d %d" %(b, a, c))
    else :
       print("%d %d %d" %(b, c, a))
else :
    if (a < b) :
       print("%d %d %d" %(c, a, b))
    else :
       print("%d %d %d" %(c, b, a))

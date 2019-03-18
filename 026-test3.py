#!/usr/bin/env python3

print("1. Celcius ke Fahrenheit\n2. Celcius ke Reamur")
cho = int(input("Masukan pilihan anda "))

if cho == 1:
    print("Celcius      Fahrenheit")
    i = 0
    while i <= 100:
        print(i, "C     (1.8 x %d)+32 = %d F" %(i, 1.8 * i + 32))
        i += 5

elif cho == 2:
    print("Celcius      Reamur")
    i = 0
    while i <= 100:
        print(i, "C       0.8 x %d = %d R" %(i, 0.8 * i))
        i += 10

else:
    quit(1)

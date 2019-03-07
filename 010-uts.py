#!/usr/bin/env python3

uts = int(input("Masukkan nilai uts "))
uas = int(input("Masukkan nilai uas "))
tugas = int(input("Masukkan nilai tugas "))

na=(uts * 0.4) + (tugas * 0.1) + (uas * 0.5)

if (na > 80 and na <= 100) :
    print("Nilai %2.2f adalah A\nPredikat sangat memuaskan" %(na))
elif (na > 60 and na <= 80) :
    print("Nilai %2.2f adalah B\nPredikat memuaskan" %(na))
elif (na > 40 and na <= 60) :
    print("Nilai %2.2f adalah C\nPredikat cukup memuaskan" %(na))
elif (na > 20 and na <= 40) :
    print("Nilai %2.2f adalah D\nPredikat tidak memuaskan" %(na))
elif (na > 0 and na <= 20) :
    print("Nilai %2.2f adalah E\nPredikat sangat tidak memuaskan" %(na))
else :
    print("Ada masalah saat mengelola data!\nExpected 0 <= na <= 100; got %2.2f" %(na))
    exit(1)

print("Selamat atas nilai Anda")

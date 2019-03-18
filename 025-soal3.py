#!/usr/bin/env python3

import os

print("1. increment kelipatan 3 dan ganjil\n2. decrement genap")
cho = int(input("Masukan pilihan anda "))

print()

if cho == 1:
    total = 0

    for i in range (0, 21):
        if (i % 3 == 0 and i % 2 != 0):
            print(i, "---> bilangan 3 dan ganjil")
            total = total + i
        else:
            print(i)

    print("Total kelipatan 3 dan ganjil adalah", total)


elif cho == 2:
    # Nothing to do
    os.system('clear')
    quit()

#!/usr/bin/env python3

def test(x, total):
    if x > 0:
        print("Data ke", x)
        total = total * x
        x = x - 1
        return test(x, total)
    else:
        return total

print("Hasil", test(3, 1))

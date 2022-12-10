from math import sqrt

a = float(input("Длина большего основания:"))
b = float(input("Длина меньшего основания:"))
h = float(input("Высота:"))
print("P =", a + b + 2 * sqrt(pow(h, 2) + pow((a - b) / 2, 2)))

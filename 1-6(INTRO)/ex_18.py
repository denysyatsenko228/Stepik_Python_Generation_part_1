"""
Только + 🌶️
Напишите программу, которая считывает три числа и подсчитывает сумму только
положительных чисел.
"""
a, b, c = int(input()), int(input()), int(input())
summa = 0
if a > 0:
    summa += a
if b > 0:
    summa += b
if c > 0:
    summa += c
print(summa)
"""
Пол и потолок
Напишите программу, которая принимает на вход действительное число
x и вычисляет по нему значение:
"""
from math import floor, ceil
x = float(input())

print(ceil(x) + floor(x))

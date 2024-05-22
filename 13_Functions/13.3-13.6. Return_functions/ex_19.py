"""
Корни уравнения 🌶️🌶️
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
a, b, c – коэффициенты квадратного уравнения ax^2 + bx + c = 0 и возвращает его корни в порядке возрастания.
"""
from math import sqrt


def solve(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b - sqrt(discr)) / (2 * a)
        x2 = (-b + sqrt(discr)) / (2 * a)
        if x1 > x2:
            return x2, x1
        else:
            return x1, x2
    elif discr == 0:
        x1 = -b / (2 * a)
        return x1, x1


print(*solve(float(input()), float(input()), float(input())))
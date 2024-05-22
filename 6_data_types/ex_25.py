"""
Квадратное уравнение 🌶️🌶️
Даны три вещественных числа a, b, c. Напишите программу, которая находит
вещественные корни квадратного уравнения:
Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
"""
from math import sqrt

a, b, c = float(input()), float(input()), float(input())
discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b - sqrt(discr)) / (2 * a)
    x2 = (-b + sqrt(discr)) / (2 * a)
    if x1 > x2:
        print(x2)
        print(x1)
    else:
        print(x1)
        print(x2)
elif discr == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print("Нет корней")

"""
Евклидово расстояние
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
"""
from math import sqrt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
res = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(res)

"""
Средние значения
Программа должна вывести 4 числа – среднее арифметическое, геометрическое,
гармоническое и квадратичное.
"""
from math import sqrt

a, b = float(input()), float(input())
arifmetich = (a + b) / 2
geometr = sqrt(a * b)
garmoni = (2 * a * b) / (a + b)
kvadratich = sqrt((a ** 2 + b ** 2) / 2)
print(arifmetich)
print(geometr)
print(garmoni)
print(kvadratich)

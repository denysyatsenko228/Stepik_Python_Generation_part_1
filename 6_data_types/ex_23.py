"""
Тригонометрическое выражение
Напишите программу, вычисляющую значение тригонометрического выражения по заданному числу градусов x.
"""

from math import sin, cos, tan, pi

x = float(input())
r = x * pi / 180
res = sin(r) + cos(r) + tan(r) * tan(r)
print(res)

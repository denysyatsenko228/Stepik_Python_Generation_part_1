"""
На вход программе подается натуральное число n.
Напишите программу, которая вычисляет значение выражения:
"""
from math import log

n = 10
sum = 0
for i in range(1, n+1):
    sum += (1 / i)
print(sum - log(n))

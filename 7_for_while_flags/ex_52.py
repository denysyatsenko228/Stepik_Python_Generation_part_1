"""
Сумма факториалов
Дано натуральное число n. Напишите программу, которая выводит значение суммы:
1!+2!+3!+…+n!
"""
from math import factorial
n = int(input())
my_factorials = 0
for i in range(1, n+1):
    my_factorials += factorial(i)
print(my_factorials)

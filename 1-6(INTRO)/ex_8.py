"""
Дано трехзначное число abc, в котором все цифры различны.Напишите программу,
которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
"""
n = int(input())
first = n // 100 % 10
second = n // 10 % 10
third = n % 10
print(first, second, third, sep="")
print(first, third, second, sep="")
print(second, first, third, sep="")
print(second, third, first, sep="")
print(third, first, second, sep="")
print(third, second, first, sep="")

"""
Обратный порядок 2
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
"""
n = int(input())
while n != 0:
    last_digit = n % 10
    print(last_digit, end="")
    n = n // 10

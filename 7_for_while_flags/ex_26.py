"""
Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет,
состоит ли указанное число из одинаковых цифр.
"""
n = int(input())
last = n % 10
flag = True

while n != 0:
    last_digit = n % 10
    if last_digit != last:
        flag = False
    n = n // 10

if flag:
    print("YES")
else:
    print("NO")

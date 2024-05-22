"""
Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли
последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
"""
n = int(input())
last = n % 10
flag = True

while n != 0:
    last_digit = n % 10
    if last_digit < last:
        flag = False
    last = last_digit
    n = n // 10

if flag:
    print("YES")
else:
    print("NO")

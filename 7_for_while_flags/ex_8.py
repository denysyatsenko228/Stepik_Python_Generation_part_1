"""
Без нулей
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
"""
total = 1
for _ in range(10):
    i = int(input())
    if i != 0:
        total *= i

print(total)
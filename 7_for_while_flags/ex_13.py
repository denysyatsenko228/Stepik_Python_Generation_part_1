"""
Последовательность Фибоначчи 🌶️
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
"""
n, f1, f2 = int(input()), 1, 1
for i in range(n):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2

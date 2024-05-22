"""
Напишите программу, которая проверяет, что для заданного четырехзначного
числа выполняется следующее соотношение: сумма первой и последней цифр равна
разности второй и третьей цифр.
"""


my_input = int(input())
fourth = my_input % 10
third = my_input // 10 % 10
second = my_input // 100 % 10
first = my_input // 1000 % 10
if fourth + first == second - third:
    print("ДА")
else:
    print("НЕТ")

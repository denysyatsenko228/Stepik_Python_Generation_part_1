"""
Диаграмма
На вход программе подается строка текста, содержащая целые числа. Напишите программу,
которая по заданным числам строит столбчатую диаграмму.
"""
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
    print("+" * s[i])
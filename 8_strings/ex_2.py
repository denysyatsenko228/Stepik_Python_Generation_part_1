"""
В столбик 2
На вход программе подается одна строка. Напишите программу, которая выводит
в столбик элементы строки в обратном порядке.
"""
s = input()
for i in range(-1, -len(s) - 1, -1):
    print(s[i])
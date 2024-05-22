"""
Нижний регистр
На вход программе подается строка. Напишите программу, которая подсчитывает
количество буквенных символов в нижнем регистре.
"""
s = input()
albhabet = "abcdefghijklmnopqrstuvwxyz"
total = 0
for i in s:
    if i in albhabet:
        total += 1
print(total)

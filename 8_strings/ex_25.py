"""
Количество слов
На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом.
Напишите программу, которая подсчитывает количество слов в ней.
"""
s = input()
s = s.count(" ")
print(s + 1)
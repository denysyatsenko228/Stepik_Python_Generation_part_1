"""
Наименьший делитель
На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.
"""
n = int(input())
for i in range(2, n+1):
    if n % i == 0:
        print(i)
        break

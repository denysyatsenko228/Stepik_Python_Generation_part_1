"""
Звездная рамка
На вход программе подается натуральное число n. Напишите программу,
которая печатает звездную рамку размерами n×19.
"""
n = int(input())
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * 19)
    else:
        print("*" + " " * 17 + "*")

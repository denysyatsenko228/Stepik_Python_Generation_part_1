"""
Без дубликатов
На вход программе подается натуральное число n, а затем n строк. Напишите программу,
которая выводит только уникальные строки, в том же порядке, в котором они были введены.
"""
n = int(input())
res = []
for _ in range(n):
    i = input()
    if i in res:
        continue
    else:
        res.append(i)
print(*res, sep="\n")
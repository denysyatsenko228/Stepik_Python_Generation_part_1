"""
Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа.
Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.

2й вариант
seq = []
for el in input().split():
    seq.append(int(el))
"""
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
max_s = s.index(max(s))
min_s = s.index(min(s))
s[min_s], s[max_s] = s[max_s], s[min_s]
print(*s)

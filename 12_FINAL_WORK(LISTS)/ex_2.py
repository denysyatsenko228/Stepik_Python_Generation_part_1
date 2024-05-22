"""
Сумма двух списков
На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M.
Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов
списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.

2й вариант
a = input().split()
b = input().split()
n = len(a)
seq = [int(a[i]) + int(b[i]) for i in range(n)]
print(*seq)
"""
L_input = input().split()
M_input = input().split()
L = [int(number) for number in L_input]
M = [int(number) for number in M_input]
summa = []
for i in range(len(L)):
    summa.append(L[i] + M[i])
print(" ".join(str(x) for x in summa))

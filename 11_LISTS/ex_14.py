"""
Символы всех строк
На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая создает список из символов всех строк, а затем выводит его.
"""
n = int(input())
res = ""
for _ in range(n):
    i = input()
    res += i
print(list(res))
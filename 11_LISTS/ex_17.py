"""
Google search - 1
На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
апишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
"""
n = int(input())
my_input = []
for _ in range(n):
    s = input()
    my_input.append(s)
need = input()
for i in my_input:
    if need.lower() in i.lower():
        print(i)

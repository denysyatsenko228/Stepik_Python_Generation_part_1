"""
На вход программе подается натуральное число n, а затем n целых чисел, каждое на
отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел
(не включая само число n).
"""
n = int(input())
cnt = 0
for _ in range(n):
    i = int(input())
    cnt += i
print(cnt)



"""
Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое
из них четным или нет.
2й вариант
flag = True
for _ in range(10):
    n = int(input())
    if n % 2 == 1:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
"""
counter = 0
for _ in range(10):
    i = int(input())
    if i % 2 == 0:
        counter += 1
if counter == 10:
    print("YES")
else:
    print("NO")

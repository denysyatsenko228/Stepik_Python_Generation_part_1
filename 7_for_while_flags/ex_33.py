"""
Следуй правилам
На вход программе подается натуральное число n. Напишите программу, которая выводит числа от
1 до n включительноза исключением:
чисел от 5 до 9 включительно;
чисел от 17 до 37 включительно;
чисел от 78 до 87 включительно.
"""
n = int(input())
for i in range(1, n+1):
    if i in range(5, 10):
        continue
    if i in range(17, 38):
        continue
    if i in range(78, 88):
        continue
    print(i)


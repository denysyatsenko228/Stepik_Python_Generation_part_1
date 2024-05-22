"""
Ход коня
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с
первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер
столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из
первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
delta_x = x2 - x1
delta_y = y2 - y1
if delta_x < 0:
    delta_x = -delta_x
if delta_y < 0:
    delta_y = -delta_y
if (delta_x == 2 and delta_y == 1) or (delta_x == 1 and delta_y == 2):
    print("YES")
else:
    print("NO")

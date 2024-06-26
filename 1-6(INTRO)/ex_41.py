"""
Ход слона 🌶️
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с
первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер
столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из
первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.
"""
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
delta_x = x2 - x1
delta_y = y2 - y1
if delta_x < 0:
    delta_x = -delta_x
if delta_y < 0:
    delta_y = -delta_y
if delta_x == delta_y:
    print("YES")
else:
    print("NO")


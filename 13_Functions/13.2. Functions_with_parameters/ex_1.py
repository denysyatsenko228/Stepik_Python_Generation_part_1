"""
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.
"""


# объявление функции
def draw_triangle(fill, base):
    for i in range(base//2 + 1):
        print(fill * (i+1))
    for i in range(base//2, -1, -1):
        print(fill * i)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

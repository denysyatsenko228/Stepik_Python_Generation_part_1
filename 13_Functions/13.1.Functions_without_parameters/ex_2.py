"""
Звездный треугольник 1
Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными
10 в соответствии с образцом:
"""


def draw_triangle():
    for i in range(10):
        for j in range(i+1):
            print("*", end="")
        print()


draw_triangle()

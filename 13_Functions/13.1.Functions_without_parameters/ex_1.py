"""
Звездный прямоугольник 1
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
"""


def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print("*" * 10)
        else:
            print("*        *")


draw_box()

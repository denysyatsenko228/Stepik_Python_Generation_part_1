"""
Звездный треугольник 🌶️
Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник
с основанием и высотой равными 15 и 8 соответственно:
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
"""


def draw_triangle():
    height = 8
    max_width = 15
    for i in range(height):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * ((max_width - len(stars)) // 2)
        print(spaces + stars)


draw_triangle()
"""
Напишите программу, которая считает стоимость трех компьютеров,
состоящих из монитора, системного блока, клавиатуры и мыши.
I will skip all easy exercises.
"""

monitor, pc, keyboard, mouse = int(input()), int(input()), int(input()), int(input())
print(3 * (monitor + pc + keyboard + mouse))


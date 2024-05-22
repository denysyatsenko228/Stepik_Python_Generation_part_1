"""
Даны три различных целых числа. Напишите программу, которая находит серединное
значение из этих чисел.
"""

a, b, c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
    print(b)
elif c < a < b or b < a < c:
    print(a)
else:
    print(c)

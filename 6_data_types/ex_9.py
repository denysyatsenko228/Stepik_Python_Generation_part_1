"""
Сортировка трех 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.
Мое альтернативное решени
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))
"""
a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    max_val = a
    if b >= c:
        mid_val = b
        min_val = c
    else:
        mid_val = c
        min_val = b
elif b >= a and b >= c:
    max_val = b
    if a >= c:
        mid_val = a
        min_val = c
    else:
        mid_val = c
        min_val = a
else:
    max_val = c
    if a >= b:
        mid_val = a
        min_val = b
    else:
        mid_val = b
        min_val = a
print(max_val)
print(mid_val)
print(min_val)
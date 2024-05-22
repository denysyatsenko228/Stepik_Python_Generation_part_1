"""
Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и
самое длинное название города.
"""
a, b, c = input(), input(), input()
min_str = min(a, b, c, key=len)
max_str = max(a, b, c, key=len)
print(min_str)
print(max_str)

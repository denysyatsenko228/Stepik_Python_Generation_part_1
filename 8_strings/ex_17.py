"""
Две половинки
На вход программе подается строка текста. Напишите программу, которая разреже
ее на две равные части, переставит их местами и выведет на экран.
"""
s = input()
if len(s) % 2 == 1:
    half_index = len(s) // 2 + 1
else:
    half_index = len(s) // 2

first_half = s[:half_index]
second_half = s[half_index:]
print(second_half + first_half)


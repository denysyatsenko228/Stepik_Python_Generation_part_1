"""
Римские цифры
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число
находится вне диапазона 1−10, то программа должна вывести текст «ошибка».
"""
n = int(input())
if 1 <= n <= 10:
    if n == 1:
        print("I")
    elif n == 2:
        print("II")
    elif n == 3:
        print("III")
    elif n == 4:
        print("IV")
    elif n == 5:
        print("V")
    elif n == 6:
        print("VI")
    elif n == 7:
        print("VII")
    elif n == 8:
        print("VIII")
    elif n == 9:
        print("IX")
    elif n == 10:
        print("X")
else:
    print("ошибка")

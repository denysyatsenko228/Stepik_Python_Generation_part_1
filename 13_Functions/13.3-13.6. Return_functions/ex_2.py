"""
Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер
месяца и возвращает количество дней в данном месяце.
"""


def get_days(month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 28
    else:
        return 31


num = int(input())

print(get_days(num))

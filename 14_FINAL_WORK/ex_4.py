"""
Магические даты
Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.
Напишите функцию is_magic(date), которая принимает в качестве аргумента строковое представление
корректной даты и возвращает значение True, если дата является магической и False - в противном случае.
"""


def is_magic(date):
    day, month, year = date.split(".")
    if int(day) * int(month) == int(year[2:]):
        return True
    else:
        return False


print(is_magic(input()))

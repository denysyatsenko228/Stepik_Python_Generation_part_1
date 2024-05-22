"""
Делители 1
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное
число и возвращающую список всех делителей данного числа.
"""


# объявление функции
def get_factors(num):
    res = []
    for i in range(1, num+1):
        if num % i == 0:
            res.append(i)
    return res


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
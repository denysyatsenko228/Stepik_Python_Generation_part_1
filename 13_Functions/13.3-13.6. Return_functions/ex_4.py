"""
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число
и возвращающую количество делителей данного числа.
"""


def get_factors(num):
    res = []
    for i in range(1, num+1):
        if num % i == 0:
            res.append(i)
    return res


def number_of_factors(num):
    return len(get_factors(num))


n = int(input())

print(number_of_factors(n))

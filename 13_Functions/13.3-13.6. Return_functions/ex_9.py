"""
Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное
число и возвращает значение True если число является простым и False в противном случае.
"""


def is_prime(n):
    flag = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            flag = False
    if n > 1 and flag == True:
        return True
    else:
        return False


print(is_prime(int(input())))

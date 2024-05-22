"""
Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента
натуральное число num и возвращает первое простое число большее числа num.
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


def get_next_prime(n):
    n += 1
    while is_prime(n) == False:
        n += 1
    return n


print(get_next_prime(int(input())))

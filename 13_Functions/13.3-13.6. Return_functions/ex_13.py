"""
BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое
значение пароля password и возвращает значение True, если пароль является действительным паролем
BEEGEEK банка и False - в противном случае.
"""


def is_palindrome(a):
    a_str = str(a)
    return a_str == a_str[::-1]


def is_simple(b):
    for i in range(2, b):
        if b % i != 0:
            return True
        else:
            return False


def is_even(c):
    return c % 2 == 0


def is_valid_password(password):
    if len(password) != 3:
        return False

    a, b, c = password
    a, b, c = int(a), int(b), int(c)
    return is_palindrome(a) and is_simple(b) and is_even(c)


print(is_valid_password(password=input().replace(":", " ").split()))


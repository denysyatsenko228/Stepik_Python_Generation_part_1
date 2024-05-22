"""
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое
число num и выводит на печать сумму его цифр.
"""


# объявление функции
def print_digit_sum(num):
    my_list = [int(i) for i in str(num)]
    print(sum(my_list))


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)

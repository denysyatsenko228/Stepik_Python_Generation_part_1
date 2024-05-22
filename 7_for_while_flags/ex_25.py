"""
Вторая цифра
Дано натуральное число n(n>9). Напишите программу, которая определяет
его вторую (с начала) цифру.
"""
n = int(input())
second_digit = n % 10
while n > 9:
    last_digit = n % 10
    n = n // 10
    second_digit = last_digit

print(second_digit)

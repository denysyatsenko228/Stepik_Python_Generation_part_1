"""
Ревью кода-6
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр
введенного числа. Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 3). Известно, что каждая ошибка затрагивает только одну строку и
может быть исправлена без изменения других строк. 1 + 1
"""
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10

print(product)
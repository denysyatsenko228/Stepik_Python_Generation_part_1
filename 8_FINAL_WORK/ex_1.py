"""
Cоберите программу, вычисляющую сумму цифр введенного натурального числа.
"""
n = int(input())
total = 0
while n != 0:
    last = n % 10
    total += last
    n = n // 10
print(total)
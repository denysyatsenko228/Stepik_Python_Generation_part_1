"""
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
"""
n = int(input())
original_n = n
total = 0
cnt = 0
dobutok = 1

while n != 0:
    last_digit = n % 10
    total += last_digit
    cnt += 1
    dobutok *= last_digit
    n = n // 10


print(total)
print(cnt)
print(dobutok)
print(total/cnt)
print(last_digit)
print((original_n % 10) + last_digit)





"""
Делители-1 🌶️
На вход программе подается два натуральных числа a, b (a< b). Напишите программу,
которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей и сумму его делителей.
Если таких чисел несколько, то выведите наибольшее из них.
"""
a, b = int(input()), int(input())
summa = 0
total = 0
for x in range(a, b+1):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += i
    if count >= summa:
        summa = count
        total = x
print(total, summa)

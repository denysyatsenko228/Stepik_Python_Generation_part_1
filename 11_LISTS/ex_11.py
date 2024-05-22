"""
Суммы двух
На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел. Напишите программу,
которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
"""
n = int(input())
numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)
res = []
for i in range(n - 1):  # Loop from 0 to n-2, so that we don't go out of bounds
    sum_of_pair = numbers[i] + numbers[i + 1]
    res.append(sum_of_pair)
print(res)
"""
Наибольшие числа 🌶️🌶️
На вход программе подается натуральное число n, а затем n различных натуральных чисел последовательности,
каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число
последовательности.
"""
n = int(input())
largest = 0
second_largest = 0
for _ in range(n):
    i = int(input())
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i

print(largest)
print(second_largest)

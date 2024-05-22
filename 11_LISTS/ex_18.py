"""
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу,
которая для каждого введенного числа x выводит значение функции f(x) = x**2 + 2x + 1, каждое на отдельной строке.
"""
n = int(input())
numbers = []
for _ in range(n):
    i = int(input())
    numbers.append(i)
print(*numbers, sep="\n")
print()
for num in numbers:
    func = num ** 2 + 2 * num + 1
    print(func)

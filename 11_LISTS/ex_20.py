"""
Negatives, Zeros and Positives
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит
все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке.
Числа должны быть выведены в том же порядке, в котором они были введены.
"""
negatives = []
zeros = []
positives = []
for _ in range(int(input())):
    i = int(input())
    if i < 0:
        negatives.append(i)
    if i == 0:
        zeros.append(i)
    if i > 0:
        positives.append(i)
print(*negatives, *zeros, *positives, sep="\n")

"""
Решите уравнение в натуральных числах
28n + 30k + 31m = 365
13 12 11
"""
total = 0
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print(n, k, m)
print("Всего решений:", total)
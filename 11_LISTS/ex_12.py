"""
k-ая буква слова 🌶️🌶️
На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
k-ую букву из введенных строк на одной строке без пробелов.
"""
n = int(input())
res = []
for _ in range(n):
    s = input()
    res.append(s)
k = int(input())
result = ""
for r in res:
    if len(r) >= k:
        result += r[k-1]
    else:
        continue
print(result)

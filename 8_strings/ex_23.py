"""
Хороший оттенок
На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста
хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
"""
s = input()
s = s.lower()
if 'хорош' in s:
    print("YES")
else:
    print("NO")
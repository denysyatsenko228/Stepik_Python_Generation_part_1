"""
Добавь разделитель
На вход программе подается строка текста и строка-разделитель. Напишите программу,
которая вставляет указанный разделитель между каждым символом введенной строки текста.
print(*input(), sep=input()) - Второе решение.
"""
text = input()
separator = input()
res = separator.join(text)
print(res)
"""
Количество цифр
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
"""
s = input()
a = '0123456789'
cnt = 0
for i in s:
    if i in a:
        cnt += 1
print(cnt)
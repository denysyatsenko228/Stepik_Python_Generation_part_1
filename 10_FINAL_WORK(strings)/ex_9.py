"""
Удали меня полностью
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».
or
s = input()
print(s.replace("@", ""))
"""
s = input()
res = ""
for i in s:
    if i == "@":
        continue
    else:
        res += i
print(res)

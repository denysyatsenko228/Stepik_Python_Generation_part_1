"""
Делаем срезы 1
На вход программе подается одна строка. Напишите программу, которая выводит:
общее количество символов в строке;
исходную строку, повторенную 3 раза;
первый символ строки;
первые три символа строки;
последние три символа строки;
строку в обратном порядке;
строку с удаленным первым и последним символами.
"""
s = input()
print(len(s))
print(s*3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])

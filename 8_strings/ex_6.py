"""
Сколько раз?
На вход программе подается одна строка. Напишите программу, которая определяет,
сколько раз в строке встречаются символы + и *.
"""
s = input()
total_pluses = 0
total_star = 0
for i in range(0, len(s)):
    if s[i] in "+":
        total_pluses += 1
    if s[i] in "*":
        total_star += 1

print("Символ + встречается", total_pluses, "раз")
print("Символ * встречается", total_star, "раз")

"""
Гласные и согласные
На вход программе подается одна строка с буквами русского языка.
Напишите программу, которая определяет количество гласных и согласных звуков.
"""
s = input()
glasnie = "ауоыиэяюе"
soglasnie = "бвгджзйклмнпрстфхцчшщ"
total_glasnie = 0
total_soglasnie = 0
for i in s.lower():
    if i in glasnie:
        total_glasnie += 1
    if i in soglasnie:
        total_soglasnie += 1

print("Количество гласных букв равно", total_glasnie)
print("Количество согласных букв равно", total_soglasnie)

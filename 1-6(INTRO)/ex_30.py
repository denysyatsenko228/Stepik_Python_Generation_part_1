"""
Дан порядковый номер месяца (1,2,…, 12). Напишите программу, которая выводит
на экран количество дней в этом месяце. Принять, что год является
невисокосным.
"""
month = int(input())
days_31 = [1, 3, 5, 7, 8, 10, 12]
if month in days_31:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)

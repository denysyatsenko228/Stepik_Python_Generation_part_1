"""
Корректный email
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки (.).
Напишите программу, проверяющую корректность email адреса.
"""
my_email = input()
if "@" in my_email and "." in my_email:
    print("YES")
else:
    print("NO")

"""
.com or .ru
На вход программе подается строка текста. Напишите программу, которая проверяет,
что строка заканчивается подстрокой .com или .ru.
"""
s = input()
if s.endswith(".com") or s.endswith(".ru"):
    print("YES")
else:
    print("NO")

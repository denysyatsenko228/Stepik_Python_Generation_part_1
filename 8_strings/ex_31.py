"""
Первое и последнее вхождение
На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз,
выведите её индекс. Если она встречается два и более раза, выведите индексы её первого и последнего
хождения на одной строке, разделенные символом пробела. Если буква «f» в данной строке не встречается,
следует вывести «NO».
"""
s = input()
count_f = s.count('f')
if count_f == 1:
    print(s.find("f"))
elif count_f >= 2:
    print(s.find("f"), s.rfind("f"))
else:
    print("NO")

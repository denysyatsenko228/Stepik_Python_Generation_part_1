"""
Молодежный жаргон
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая преобразует
каждое слово введенного текста в "молодежный жаргон" по следующему правилу:
1. первая буква каждого слова удаляется и ставится в конец слова;
2. затем в конец слова добавляется слог "ки".
"""
print(*[i[1:] + i[0] + "ки" for i in input().split()])
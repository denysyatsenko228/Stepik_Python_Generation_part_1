"""
Самый частотный символ
На вход программе подается строка текста. Напишите программу,
которая выводит на экран символ, который появляется наиболее часто.
"""
s = "aaaabbc"
cnt = 0
res = ""
for i in range(len(s)):
    current_count = s.count(s[i])
    if current_count >= cnt:
        cnt = current_count
        res = s[i]
print(res)

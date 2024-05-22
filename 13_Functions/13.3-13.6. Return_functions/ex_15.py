"""
Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента
непустую строку text, состоящую из символов ( и ) и возвращает значение True если
поступившая на вход строка является правильной скобочной последовательностью и
False в противном случае.

2й вариант
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")

    return text == ""

txt = input()
print(is_correct_bracket(txt))
"""


def is_correct_bracket(text):
    if text.startswith(")") or text.endswith("("):
        return False
    cnt = 0
    for char in text:
        if char == "(":
            cnt += 1
        elif char == ")":
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        return True
    else:
        return False


txt = input()

print(is_correct_bracket(txt))
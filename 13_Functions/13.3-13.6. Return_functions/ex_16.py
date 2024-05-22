"""
Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в
«верблюжьем регистре» и преобразует его в «змеиный регистр».
"""


def convert_to_python_case(text):
    new_text = []
    for i in text:
        if i == i.lower():
            new_text.append(i)
        elif i != i.lower():
            new_text.append("_")
            new_text.append(i.lower())
    return "".join(new_text[1:])


txt = input()

print(convert_to_python_case(txt))

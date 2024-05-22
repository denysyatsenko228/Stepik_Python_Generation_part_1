"""
Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря
с сдвигом вправо на 10 символов.
"""


def encryption(text, step):
    result = []

    for char in text:
        if 'а' <= char <= 'я':
            new_char = chr((ord(char) - ord('а') + step) % 32 + ord('а'))
        elif 'А' <= char <= 'Я':
            new_char = chr((ord(char) - ord('А') + step) % 32 + ord('А'))
        elif 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + step) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + step) % 26 + ord('A'))
        else:
            new_char = char
        result.append(new_char)

    return ''.join(result)


text, step = input(), int(input())

print(encryption(text, step))

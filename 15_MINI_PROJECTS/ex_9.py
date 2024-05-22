"""
Аве, Цезарь 🌶️
На вход программе подается строка текста на английском языке, в которой нужно
зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра
Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом
остаются строчными, а прописные – прописными. Гарантируется, что между
различными словами присутствует один пробел.
"""


def encryption(text, step):
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + step) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + step) % 26 + ord('A'))
        else:
            new_char = char
        result.append(new_char)

    return ''.join(result)


def encrypt_text(text):
    words = text.split(" ")
    new_words = []

    for word in words:
        step = sum(1 for char in word if char.isalpha())
        new_word = encryption(word, step)
        new_words.append(new_word)
    return " ".join(new_words)


text = input()

print(encrypt_text(text))
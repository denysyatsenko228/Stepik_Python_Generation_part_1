"""
Текст "Hawnj pk swhg xabkna ukq nqj." был получен в результате шифрования алгоритмом Цезаря с сдвигом
вправо на n символов. Расшифруйте данный текст.
Примечание. Считайте, что n∈[0;25].
"""


def decryption(text):
    results = []

    for step in range(25):
        result = []
        for char in text:
            if 'а' <= char <= 'я':
                new_char = chr((ord(char) - ord('а') - step) % 32 + ord('а'))
            elif 'А' <= char <= 'Я':
                new_char = chr((ord(char) - ord('А') - step) % 32 + ord('А'))
            elif 'a' <= char <= 'z':
                new_char = chr((ord(char) - ord('a') - step) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                new_char = chr((ord(char) - ord('A') - step) % 26 + ord('A'))
            else:
                new_char = char
            result.append(new_char)

        results.append(''.join(result))

    return '\n'.join(results)


text = input()

print(decryption(text), sep="\n")
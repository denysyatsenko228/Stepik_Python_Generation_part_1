"""
Генератор безопасных паролей
Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
а также на то, какие символы требуется в него включить, а какие исключить.
"""
import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""

cnt_passwords = int(input("Укажите количество паролей для генерации: \n"))
len_passwords = int(input("Укажите длину одного пароля: \n"))
is_digits_in_password = input("Включать ли цифры 0123456789 да/нет \n")
is_upper_cases = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ да/нет \n")
is_lower_cases = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz да/нет \n")
is_punctuation = input("Включать ли символы !#$%&*+-=?@^_ да/нет \n")
optional_symbols = input("Исключать ли неоднозначные символы il1Lo0O да/нет \n")

if is_digits_in_password == "да":
    chars += digits
if is_upper_cases == "да":
    chars += uppercase_letters
if is_lower_cases == "да":
    chars += lowercase_letters
if is_punctuation == "да":
    chars += punctuation
if optional_symbols == "да":
    for c in "il1Lo0O":
        chars.replace(c, "")


def generate_password(length, chars):
    passwords = []
    for _ in range(cnt_passwords):
        password = "".join(random.sample(chars, length))
        passwords.append(password)
    return "\n".join(passwords)


print(generate_password(len_passwords, chars))

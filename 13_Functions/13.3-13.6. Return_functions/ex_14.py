"""
Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве
аргумента строковое значение пароля password и возвращает значение True,
если пароль является надежным и False - в противном случае.
Пароль является надежным если:
его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
"""


def is_password_good(password):
    if len(password) < 8:
        return False

    upper_count = 0
    lower_count = 0
    digit_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1

    return upper_count > 0 and lower_count > 0 and digit_count > 0


# Пример использования
txt = input()
print(is_password_good(txt))

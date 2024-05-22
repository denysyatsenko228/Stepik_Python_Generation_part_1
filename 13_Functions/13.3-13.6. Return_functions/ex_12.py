"""
Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение
True если указанный текст является палиндромом и False в противном случае.
"""


def is_palindrome(text):
    for char in text:
        if char in '.,!?- ':
            text = text.replace(char, "")
    if text == text[::-1]:
        return True
    else:
        return False


txt = input().lower()


print(is_palindrome(txt))

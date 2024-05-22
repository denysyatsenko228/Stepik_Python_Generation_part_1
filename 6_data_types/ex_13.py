"""
What's Your Name?
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
Hello <введенное имя> <введенная фамилия>! You have just delved into Python
"""
name, surname = input(), input()
print("Hello ", name, " ", surname, "! You have just delved into Python", sep="")

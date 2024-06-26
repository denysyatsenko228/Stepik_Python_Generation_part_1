"""
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.
"""


# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep="")


# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()

# вызываем функцию
print_fio(name, surname, patronymic)

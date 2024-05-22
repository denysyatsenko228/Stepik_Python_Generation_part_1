"""
Корректный ip-адрес
На вход программе подается строка текста, содержащая 4 целых неотрицательных числа, разделенных точкой.
Напишите программу, которая определяет, является ли введенная строка текста корректным ip-адресом.
"""
import ipaddress


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


ip_address = input()
if is_valid_ip(ip_address):
    print("ДА")
else:
    print("НЕТ")
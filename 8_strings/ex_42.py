"""
Шифр Цезаря 🌶️
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного
мира, поэтому ученые из НКР не могут понять, как именно нужно декодировать данные сообщения. Напишите программу для
декодирования этого шифра.
"""
n, s = int(input()), input()
for i in s:
    decryption = ord(i) - n
    if decryption < 97:
        decryption += 26
    print(chr(decryption), end="")

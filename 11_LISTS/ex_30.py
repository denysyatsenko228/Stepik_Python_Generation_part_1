"""
Все сразу 2 🌶️
Дополните приведенный код, чтобы он:
Заменил второй элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список, с помощью функции print()
"""
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
numbers.pop(0)
numbers = numbers * 2
numbers.insert(3, 25)
print(numbers)
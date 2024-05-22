"""
В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма,
предполагая, что по крайней мере n энных степеней необходимо для получения суммы,
которая сама является энной степенью для n > 2.
Напишите программу для опровержения гипотезы Эйлера (продержавшейся до 1967 года)
и найдите четыре положительных целых числа, сумма 5-х степеней которых равна
5-й степени другого положительного целого числа.
Таким образом, найдите пять натуральных чисел a, b, c, d, e, удовлетворяющих условию:
a**5 + b**5 + c**5 + d**5 = e**5
"""
total = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        total += 1
                        print('a =', a, 'b =', b, 'c =', c, 'd =', 'e =', e)
print('Общее количество натуральных решений =', total)
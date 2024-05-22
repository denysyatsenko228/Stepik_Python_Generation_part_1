"""
Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:
количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречаются цифры 0 и 5 (всего суммарно). 1332
"""
n = int(input())
cnt_3 = 0
last = n % 10
last_digit_count = 0
chetnie_cnt = 0
summa = 0
proizvedenie = 1
zeros = 0
fives = 0

while n != 0:
    last_digit = n % 10
    if last_digit == 3:
        cnt_3 += 1

    if last_digit == last:
        last_digit_count += 1

    if last_digit % 2 == 0:
        chetnie_cnt += 1

    if last_digit > 5:
        summa += last_digit

    if last_digit > 7:
        proizvedenie *= last_digit
    else:
        proizvedenie == 1

    if last_digit == 0:
        zeros += 1

    if last_digit == 5:
        fives += 1

    n //= 10


print(cnt_3)
print(last_digit_count)
print(chetnie_cnt)
print(summa)
print(proizvedenie)
print(zeros+fives)






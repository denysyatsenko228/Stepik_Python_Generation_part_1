"""
Напишите программу, которая по введённому возрасту пользователя сообщает,
к какой возрастной группе он относится:
"""
years = int(input())
if years <= 13:
    print("детство")
elif 14 <= years <= 24:
    print("молодость")
elif 25 <= years <= 59:
    print("зрелость")
else:
    print("старость")

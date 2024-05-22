"""
Цветовой микшер 🌶️
Красный, синий и желтый называются основными цветами, потому что их нельзя получить
путем смешения других цветов. При смешивании двух основных цветов получается вторичный цвет:
если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания.
Если пользователь вводит что-нибудь помимо названий «красный», «синий» или
«желтый», то программа должна вывести сообщение об ошибке. В противном случае
программа должна вывести название вторичного цвета, который получится в результате.
"""
a, b = input(), input()
my_list = ["красный", "синий", "желтый"]
if a in my_list and b in my_list:
    if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
        print("фиолетовый")
    elif (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
        print("оранжевый")
    elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
        print("зеленый")
    else:
        print(a)
else:
    print("ошибка цвета")
"""
До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности
является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). При этом сами слова «КОНЕЦ» и
«конец» не входят в последовательность, лишь символизируя её окончание. Напишите программу, которая выводит члены
данной последовательности.
"""
text = input()
while text != "КОНЕЦ" and text != "конец":
    print(text)
    text = input()
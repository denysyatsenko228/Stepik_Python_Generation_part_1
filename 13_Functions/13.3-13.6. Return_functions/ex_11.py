"""
Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и False в
противном случае.
"""


def is_one_away(word1, word2):
    cnt = 0
    if len(word1) != len(word2) or word1 == word2:
        return False
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt > 1:
            return False
    else:
        return True


print(is_one_away(input(), input()))

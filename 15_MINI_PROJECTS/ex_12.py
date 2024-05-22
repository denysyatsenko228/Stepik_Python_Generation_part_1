"""
Угадайка слов
Описание проекта: программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова
неизвестны. Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове. Если такой
буквы нет, к виселице добавляется круг в петле, изображающий голову. Пользователь продолжает отгадывать буквы до
тех пор, пока не отгадает всё слово. За каждую неудачную попытку добавляется еще одна часть туловища висельника
(обычно их 6: голова, туловище, 2 руки и 2 ноги.
"""


import random
word_list = [
    'молоко', 'яблоко', 'собака', 'кошка', 'город', 'дерево',
    'школа', 'учитель', 'книга', 'стол', 'стул', 'окно',
    'дверь', 'река', 'озеро', 'машина', 'самолёт', 'поезд',
    'дом', 'квартира'
]


def get_word():
    word = random.choice(word_list)
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O   DIED!
           |     ⎛▼⎞
           |     ⎛ ⎞
           |    
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ 
           |
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |
           |
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     ⎛▼
           |
           |
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      ▼
           |
           |
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    tries = 6
    word_completion = '_' * len(word)
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов

    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже называли эту букву.")
            elif guess not in word:
                print("Такой буквы нету, попробуйте еще.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отличная работа!", guess, "есть в этом слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже называли это слово", guess)
            elif guess != word:
                print("Данное слово не верное.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Введите букву или слово.")
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print("Поздравляю! Вы угадали слово!")
    else:
        print("Вы не угадали слово! Это было:", word, "Поэтому вы мертвы(")


play(get_word())

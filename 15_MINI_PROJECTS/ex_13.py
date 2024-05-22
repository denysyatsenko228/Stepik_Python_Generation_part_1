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
    stages = [
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ ⎞
           |    
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ 
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     ⎛▼
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      ▼
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
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
    guessed = False
    guessed_letters = []
    guessed_words = []

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
                print("Такой буквы нет, попробуйте еще.")
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
                print("Данное слово неверное.")
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

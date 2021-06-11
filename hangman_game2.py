import random

def find_occurence(word, letter):
    store = []
    for i in range(len(word)):
        if word[i] == letter:
            store.append(i)
    return store

def blanks_filled(guess, word, blank):
    empty = ''
    index_store = find_occurence(word, guess)

    for i in range(len(word)):
        if i in index_store:
            empty += guess
        else:
            empty += blank[i]
    return empty

def hangman():

    word_bank = ['calculator','awkward', 'dwarves', ' hyphen', 'ostracize', 'zombie', 'oxygen']

    i = len(word_bank)
    random_word = word_bank[random.randint(0, i-1)]

    random_word2 = ''
    for k in range(len(random_word)):
        random_word2 += ' ' + random_word[k]
    #print(random_word2)

    blanks = ''
    i = 0
    while i != len(random_word2):
        if random_word2[i] == ' ':
            blanks += ' '
        else:
            blanks += '_'
        i += 1
    print(blanks)
    used_letters = []

    counter = 0
    while counter != 8:
        guess = input("guess:")
        if guess in random_word2:
            print('GOOD GUESS!')
            print('Used letters:', used_letters)
            a = blanks_filled(guess, random_word2, blanks)
            print(a)
            blanks = a
            counter += 0
            #hangman_drawing(counter)
            if '_' not in a:
                print('YOU WON!!!!!')
                break
            else:
                continue
        else:
            print('TOO BAD...')
            if guess not in used_letters:
                used_letters += guess
            else:
                used_letters = used_letters
            print('Used letters:', used_letters)
            counter += 1
            a = blanks_filled(guess, random_word2, blanks)
            print(a)
            hangman_drawing(counter)
    print("Word: ", random_word2)
    return None


def hangman_drawing(counter):
    if counter == 1:
        print('\n' * 4, '=========')

    elif counter == 2:
        print('     + ---|', '\n', '    |', '\n', '    |', '\n', '    |', '\n', '    |', '\n', '=========')

    elif counter == 3:
        print('     + ---|', '\n', '    |    O', '\n', '    |', '\n', '    |', '\n', '    |', '\n', '=========')

    elif counter == 4:
        print('     + ---|', '\n', '    |    O', '\n', '    |    |', '\n', '    |', '\n', '    |', '\n', '=========')

    elif counter == 5:
        print('     + ---|', '\n', '    |    O', '\n', '    |   /|', '\n', '    |', '\n', '    |', '\n', '=========')

    elif counter == 6:
        print('     + ---|', '\n', '    |    O', '\n', '    |   /|\ ', '\n', '    |', '\n', '    |', '\n', '=========')

    elif counter == 7:
        print('     + ---|', '\n', '    |    O', '\n', '    |   /|\ ', '\n', '    |   /', '\n', '    |', '\n', '=========')

    elif counter == 8:
        print('     + ---|', '\n', '    |    O', '\n', '    |   /|\ ', '\n', '    |   / \ ', '\n', '    |', '\n',
              '=========')
        print('YOU LOST!!!!! NOOOB!!!!')

hangman()
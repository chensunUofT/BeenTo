import random


def greet(mode, name='Bim', location='Nowhere'):

    hello_words_list = ['Hello', 'Aloha', 'Bonjour', '你好']
    hello_word = random.choice(hello_words_list)

    if mode == 'name':
        return("{}, {}!".format(hello_word, name))
    elif mode == 'location':
        return("{}, user from {}!".format(hello_word, location))
    else:
        return("Not a correct mode selected. Hello anyway!")
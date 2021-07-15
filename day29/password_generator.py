import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'
PASSWORD_LENGTH = 24


def generate_password():
    vocabulary = ''.join((LETTERS, NUMBERS, SYMBOLS))
    password = [random.choice(vocabulary) for _ in range(PASSWORD_LENGTH)]
    random.shuffle(password)
    return ''.join(password)

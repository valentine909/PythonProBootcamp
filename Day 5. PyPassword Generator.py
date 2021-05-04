LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+,-.:;<=>?@[]^_{|}~'


def get_settings():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    return nr_letters, nr_numbers, nr_symbols


def generate_password(counts: tuple):
    import random
    vocabulary = [LETTERS, NUMBERS, SYMBOLS]
    password = []
    for index, item in enumerate(vocabulary):
        password += [item[random.randint(0, len(item) - 1)] for _ in range(counts[index])]
    random.shuffle(password)
    print(''.join(password))


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    generate_password(get_settings())

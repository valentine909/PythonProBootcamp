import pandas as pds


def process_cvs(name: str) -> dict:
    alphabet = pds.read_csv(name)
    return {row.letter: row.code for (idx, row) in alphabet.iterrows()}


def take_input_word():
    name = input("Enter a word: ")
    while not name.isalpha():
        print('Sorry, only letters in the alphabet please')
        name = input("Enter a word: ")
    return name


def encode_word(word):
    return [alphabet_dict[letter.upper()] for letter in word]


if __name__ == '__main__':
    alphabet_dict = process_cvs('nato_phonetic_alphabet.csv')
    print(encode_word(take_input_word()))

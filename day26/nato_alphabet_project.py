import pandas as pds


def process_cvs(name: str) -> dict:
    alphabet = pds.read_csv(name)
    return {row.letter: row.code for (idx, row) in alphabet.iterrows()}


def take_input_word():
    return input("Enter a word: ")


def encode_word(word):
    return [alphabet_dict[letter.upper()] for letter in word]


if __name__ == '__main__':
    alphabet_dict = process_cvs('nato_phonetic_alphabet.csv')
    print(encode_word(take_input_word()))

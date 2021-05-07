"""
TODO 1. Choose a word
2. Guess a word
3. Win and loose conditions
"""


def convert_txt(filename='nounlist.txt'):
    """
    Converts txt file with words to list of words and dumps it to pickle
    :param filename: Path to txt file.
    :return: None.
    """
    from pickle import dump
    word_library = []
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                if '-' not in line:
                    word_library.append(line.strip())
    except FileNotFoundError:
        print("Text file with words (nounlist.txt) not found.")
        exit()
    with open('words.pickle', 'wb') as f:
        dump(word_library, f)


def restore_vocabulary(filename='words.pickle'):
    """
    Restores a pickled list of words.
    :param filename: Path to pickle file.
    :return: None.
    """
    from pickle import load
    try:
        with open(filename, 'rb') as f:
            vocabulary = load(f)
    except FileNotFoundError:
        print("Pickle file with words (words.pickle) not found. Trying to restore... Restart an application.")
        convert_txt()
        exit()
    return vocabulary


def choose_word(list_of_words: list) -> str:
    """
    Choose a random word from the list
    :param list_of_words:  List of 'words'.
    :return: Random word as string.
    """
    from random import choice
    return choice(list_of_words)


def game():
    from day7_stages import stages
    word = choose_word(restore_vocabulary())
    hidden_word_list = ['_'] * len(word)
    hidden_word = ''.join(hidden_word_list)
    lives = len(stages)
    chosen_letters = []
    while lives and not hidden_word == word:
        chosen_letters.sort()
        chosen_letters_str = ', '.join(chosen_letters)
        print(f"You\'ve picked the following letters: {chosen_letters_str}")
        letter = input(f"Guess a word:\n{hidden_word}\nGuess a letter:\n").lower()
        chosen_letters.append(letter)
        is_guessed = False
        for position, char in enumerate(word):
            if letter == char:
                hidden_word_list[position] = letter
                is_guessed = True
        hidden_word = ''.join(hidden_word_list)
        if not is_guessed:
            lives -= 1
            print(stages[lives])
    print(f"The word is: {word}")
    if lives:
        print("You win!")
    else:
        print("You loose!")


if __name__ == '__main__':
    game()

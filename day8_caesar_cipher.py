from day8_art import logo
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def take_input():
    mode = input("Type 'encode' to encrypt, type 'decode' to decode:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    return mode, message.lower(), shift


def cryptographer():
    mode, message, shift = take_input()
    new_message = ''
    shift %= 26
    direction = 1 if mode == 'encode' else -1
    for i in message:
        if i.isalpha():
            new_position = (ALPHABET.index(i) + shift * direction) % 26
            new_message += ALPHABET[new_position]
        else:
            new_message += i
    return new_message


if __name__ == '__main__':
    print(logo)
    loop_flag = True
    while loop_flag:
        print(cryptographer())
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if again == 'no':
            loop_flag = False
            print("Goodbye!")

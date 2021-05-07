def take_input():
    mode = input("Type 'encode' to encrypt, type 'decode' to decode:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    return mode, message.lower(), shift


def encode(message, shift):
    new_message = ''
    for i in message:
        new_position = (ord(i) + shift) - (ord(i) + shift) // (97 + 25) * 25
        new_message += chr(new_position)
    return new_message


def decode(message, shift):
    new_message = ''
    for i in message:
        if ord(i) - shift < 97:
            new_position = (ord(i) - shift) + 25
        else:
            new_position = (ord(i) - shift)
        new_message += chr(new_position)
    return new_message


def cryptographer():
    mode, message, shift = take_input()
    if mode == 'encode':
        print(encode(message, shift))
    elif mode == 'decode':
        print(encode(message, shift))
    else:
        print("Clarify your input")


if __name__ == '__main__':
    cryptographer()

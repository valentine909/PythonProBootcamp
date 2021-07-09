with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter_sample = file.read()

with open('./Input/Names/invited_names.txt', 'r') as file:
    names = file.read()

for name in names.split('\n'):
    with open(f'./Output/ReadyToSend/letter_for_{name}. txt', 'w') as file:
        text = letter_sample.replace('[name]', name)
        file.write(text)

from translate import Translator
import csv

translator = Translator(to_lang='ru')

with open('data/vocabulary_5001-6000.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('English', 'Russian'))

with open('words_5001-6000.txt', 'r') as file:
    words = file.readlines()
for word in words:
    word = word.strip()
    trans = translator.translate(word)
    with open('data/vocabulary_5001-6000.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((word, trans))


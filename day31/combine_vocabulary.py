import csv


with open('words_5001-6000.txt', 'r', encoding='utf-8') as file:
    words = [i. strip() for i in file.readlines()]


with open('words_5001-6000_trans.txt', 'r', encoding='utf-8') as file:
    trans = [i. strip() for i in file.readlines()]

with open('data/vocabulary_5001-6000.csv', 'a', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('English', 'Russian'))
    for line in zip(words, trans):
        writer.writerow(line)

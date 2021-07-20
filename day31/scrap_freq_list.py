import requests
from bs4 import BeautifulSoup


url = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/TV/2006/8001-9000'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
words = []
a = soup.find('div', 'mw-parser-output')
b = a.find('tbody')
for link in b.find_all('a'):
    word = link.string
    if ' ' not in word and not word.title() == word:
        words.append(word)
file_name = url.split('/')[-1]
with open(f'{file_name}', 'w', encoding='utf-8') as freq_words:
    freq_words.write('English\n')
    for word in words:
        try:
            freq_words.write(word + '\n')
        except UnicodeEncodeError:
            pass

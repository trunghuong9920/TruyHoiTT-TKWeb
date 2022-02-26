from re import T
import nltk
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.gutenberg.org/files/67487/67487-h/67487-h.htm'
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = nltk.word_tokenize(raw)

lists = tokens[ : 20]

dec = {}
for i  in lists:
    if i in dec:
        dec[i] += 1
    else:
        dec[i] = 1
print(dec)
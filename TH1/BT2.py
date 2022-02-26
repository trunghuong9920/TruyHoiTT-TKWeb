from re import T
import nltk
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.gutenberg.org/files/67487/67487-h/67487-h.htm'
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = nltk.word_tokenize(raw)

porter = nltk.PorterStemmer()

lists = [porter.stem(t) for t in tokens]

# ----------------
url2 = 'https://www.gutenberg.org/files/67493/67493-h/67493-h.htm'
html2 = request.urlopen(url2).read().decode('utf8')
raw2 = BeautifulSoup(html2, 'html.parser').get_text()
tokens2 = nltk.word_tokenize(raw2)

porter = nltk.PorterStemmer()

lists2 = [porter.stem(t) for t in tokens2]

# ----------------
url3 = 'https://www.gutenberg.org/files/67493/67493-h/67493-h.htm'
html3 = request.urlopen(url3).read().decode('utf8')
raw3 = BeautifulSoup(html3, 'html.parser').get_text()
tokens3 = nltk.word_tokenize(raw3)

porter = nltk.PorterStemmer()

lists3 = [porter.stem(t) for t in tokens3]

listText = [lists, lists2,lists3]

dic = {}
count = 0
for i in listText:
    count += 1
    for x in i:
        if x in dic:
            dic[x] += 1
            dic[count] += 1
        else:
            dic[x] = 1
print(dic)
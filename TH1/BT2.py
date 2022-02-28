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
url3 = 'https://www.gutenberg.org/files/67511/67511-h/67511-h.htm'
html3 = request.urlopen(url3).read().decode('utf8')
raw3 = BeautifulSoup(html3, 'html.parser').get_text()
tokens3 = nltk.word_tokenize(raw3)

porter = nltk.PorterStemmer()

lists3 = [porter.stem(t) for t in tokens3]

listText = [lists[:10], lists2[:10],lists3[:10]]
dic = dict()

for index in range(len(listText)):
    for doc in listText:
        for word in doc:
            if word in dic:
                if index in dic[word]:
                    dic[word][index] += 1
                else:
                    dic[word][index] = 1
            else:
                dic[word] = dict()
                dic[word][index] = 1

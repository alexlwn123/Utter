import requests as re
from bs4 import BeautifulSoup

def lookup(word, query="dictionary"):
    url = 'https://wordsapiv1.p.mashape.com/words/fast/' + query
    reply = re.get('https://wordsapiv1.p.mashape.com/words/fast/synonyms').text
    soup = BeautifulSoup(reply, "html.parser")
    print(soup.text)

     


if __name__ == '__main__':
    lookup("dog")
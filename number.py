import requests as re
import random
from bs4 import BeautifulSoup


def number_trivia(number: str):
    operation = random.choice(["math", "trivia"])
    url = f"http://numbersapi.com/{number}/{operation}"
    print(url)
    reply = re.get(url)
    print(reply.text)

def get_date(month: str, day: str):
    url = f"http://numbersapi.com/{month}/{day}/date"
    reply = re.get(url)
    print(reply.text)


if __name__ == '__main__':
    number_trivia("11")

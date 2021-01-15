from bs4 import BeautifulSoup
import requests as re
import json
import random

def get_remark(routes, name):
  route = random.choice(routes)
  route = route.replace(':name', name)
  route = route.replace(':from', "God")
  route = route.replace(':noun', "coitus")
  route = route.replace(':reaction', "fuck off")
  route = route.replace(':tool', "a computer")
  route = route.replace(':company', "NCR")
  reply = re.get('https://www.foaas.com' + route).text
  soup = BeautifulSoup(reply, "html.parser")
  ans = soup.find_all('meta', limit=2)[-1]['content']
  ans = ans.replace('- God', '\n  - God')
  return ans

def insulter(name = "Alex"):
    cities = []
    text = re.get('https://www.foaas.com/operations').text
    soup = BeautifulSoup(text, "html.parser")
    obj = json.loads(str(soup))
    routes = [x['url'] for x in obj][2:]
    print(get_remark(routes, name))

if __name__ == '__main__':
    insulter()
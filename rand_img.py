import requests
from bs4 import BeautifulSoup
import random

def random_image():
    nums = list(range(2, 19))
    page_num = random.choice(nums)
    user_url1 = 'https://3d-galleru.ru/archive/cat/novye-otkrytki-top-new/'
    user_url2 = f'https://3d-galleru.ru/archive/cat/novye-otkrytki-top-new/page-{page_num}/'
    urls = [user_url1, user_url2]
    user_url = random.choice(urls)
    response = requests.get(user_url)
    soup = BeautifulSoup(response.content, 'lxml')
    images = soup.find_all("div", class_='card-image')
    m = []
    for i in images:
        s = str(i)
        ind = s.find('data-url=')
        ind2 = s.find(' src')
        s = s[ind:ind2]
        s = s[10:-1]
        m.append(s)
    
    return random.choice(m)

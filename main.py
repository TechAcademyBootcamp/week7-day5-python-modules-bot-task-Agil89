from google import google
import urllib
from bs4 import BeautifulSoup
import requests
def learningBot():
    while True:
        with open('bot.txt','a+') as f:
            f.seek(0)
            data_dict = {}
            for line in f.readlines():
                k , v = line.strip().split('::')
                data_dict[k.strip()] = v.strip()
            question = input('Sualinizi verin: ')
            if question == 'exit':
                exit()
            if question not in data_dict:
                users_answer = input('Suali mene oyretmek isteyirsiniz mi? ')
                if users_answer == 'yes':
                    answer = input('Sualiniza cavab verin: ')
                    f.write(f'{question}::{answer}\n')
                else:
                    exit()
            else:
                print(data_dict[question])

def news():
    response = requests.get('https://oxu.az/')
    soup = BeautifulSoup(response.text, features = 'html.parser')
    news_list = soup.findAll('div',{'class':'title'})
    news_links = soup.select('.news-i a')
    for x in range(len(news_list)):
        print(news_list[x].text,f"https://oxu.az/{news_links[x]['href']}")

def exchange():
    response = requests.get('https://api.exchangeratesapi.io/latest?base=TRY')
    response_dict = response.json()
    print('Turk lirasinin bu gune olan mezennesi: ')
    for x in response_dict['rates']:
        print(x,response_dict['rates'][x])


def weatherInfo():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=61389a93f65b06e891a9fac33362e797')
    response_dict = response.json()
    print(response_dict)

def googleRequest():
    text = input('Enter the phrase: ')
    # response = requests.get(f'https://www.google.com/search?q={text}')
    # print(response.content)
    # soup = BeautifulSoup(response.content, features='html.parser')
    # print(soup)
    # news_list = soup.findAll('h3')
    # news_list = soup.select('.LC20lb DKV0Md')
    # print(news_list)
    thepage = requests.get(f'https://www.google.com/search?q={text}')
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text


googleRequest()
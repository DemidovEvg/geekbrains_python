# Написать приложение, которое собирает основные новости с сайта на выбор 
# news.mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. 
# Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные новости в БД

from pprint import pprint
from lxml import html
import requests
import datetime
import pymongo
import re

def add_current_date(stime, template):
    today = datetime.datetime.now()
    date_delta = 0
    if 'вчер' in stime:
        date_delta = -1
    elif 'позавчера' in stime:
        date_delta = -2
    stime = [s for s in stime.split() if ':' in s][0]
    time = datetime.datetime.strptime(stime, template)
    return datetime.datetime(today.year,
                            today.month,
                            today.day + date_delta,
                            time.hour,
                            time.minute)

def get_news(news, news_category, block_branches):
    news[news_category] = []
    for new_branch in block_branches:
        new = {}
        new['source'] = new_branch.xpath(".//a[contains(@class, 'mg-card__source-link')]/text()")[0]
        new['title'] = new_branch.xpath(".//a[contains(@class, 'mg-card__link')]/text()")[0]
        new['title'] = new['title'].translate({ord('\xa0'): ord(' ')})
        new['annotation'] = new_branch.xpath(".//div[contains(@class, 'mg-card__annotation')]/text()")[0]
        new['annotation'] = new['annotation'].translate({ord('\xa0'): ord(' ')})
        new['link'] = new_branch.xpath(".//a[contains(@class, 'mg-card__link')]/@href")[0]
        new['time'] = add_current_date(new_branch.xpath(".//span[contains(@class, 'mg-card-source__time')]/text()")[0], "%H:%M")
        news[news_category].append(new)
    return news[news_category]

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',}
response = requests.get('https://yandex.ru/news', headers=headers)
# response = open(r'G:\000---Python\gb python\HW_info_collection\dz_5\ya.html', encoding='utf-8').read()
dom = html.fromstring(response.text)
# dom = html.fromstring(response)
main_news_branches = dom.xpath("//div[contains(@class,'news-top-flexible-stories')]/div")

date_today = datetime.datetime.today()

news = {}
news['Главные новости'] = get_news(news, 'Главные новости', main_news_branches)

all_news_branches = dom.xpath("//div[contains(@class, 'mg-top-rubric-flexible-stories')]/../div")

is_next_news_block = False
for all_news_branch in all_news_branches:
    if is_next_news_block:
        block_branches = all_news_branch.xpath(".//div[contains(@class, 'mg-card_flexible')]")
        news[news_category] = get_news(news, news_category, block_branches)
        is_next_news_block = False
    else:
        try:
            news_category = all_news_branch.xpath(".//div[contains(@class, 'news-top-rubric-heading')]//text()")[0]
            is_next_news_block = True
        except:
            continue


client = pymongo.MongoClient('localhost', 27017)
db = client.news_db
news_collection = db.news_collection

counter = 0
for category, news_in_category in news.items():
    for new in news_in_category:
            news_collection.update_one({"Категория новости": category, **new}, {'$set': {"Категория новости": category, **new}}, upsert=True) 
            counter += 1

print(f'Всего {news_collection.find({}).count()} новостей')

class Commands:
    RE_EXIT = re.compile(r"""(?P<command>(exit)|(quit)|(\\q))""", re.X)

def printer(request):
    result = news_collection.find(request)
    pprint(result)

message = """---Вывести все новости: all
---Вывести категории новостей: category
---Вывести количество новостей: count
---Вывести новости по категории: category="название категории"
---Остановить работу: exit | quit | \q"""
print(message)
command = input("Введите команду: ").lower().strip()
while not Commands.RE_EXIT.search(command):
    if 'all' in command:
        for new in news_collection.find({}):
            pprint(new)
    elif 'category' in command:
        if command == 'category':
            num = 0
            for category in news_collection.aggregate( [{"$group":{"_id": "$Категория новости"}}]):
                num += 1
                print(f"{num}-{category['_id']}")
        else:
            category = command.replace("category=", '')
            for new in news_collection.find({"Категория новости": category}):
                pprint(new)
    elif 'count' in command:
        pprint(news_collection.count_documents({}))
    else:
        print("Команда не распознана")
        print(message)
    
    command = input("Введите команду: ")     
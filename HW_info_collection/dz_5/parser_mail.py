from typing import Set, Tuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
import time
import datetime
import locale
import pymongo
import logging
from pprint import pprint
import re
import bson

logging.basicConfig(filename='example.log', 
                    format='%(name)s %(levelname)s %(funcName)s %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8', 
                    level=logging.INFO)


chrome_options = webdriver.ChromeOptions()
# открыть окно на весь экран
# chrome_options.add_argument('start-maximized')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('prefs', {"profile.managed_default_content_settings.images": 2})
# starts a new chrome session
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10) # seconds

driver.get("https://mail.ru/")

def get_element_with_wait(element, XPATH):
    return WebDriverWait(element, 10).until( 
                EC.presence_of_element_located((By.XPATH, XPATH)))

element = get_element_with_wait(element=driver, 
                XPATH="//button[text()='Войти']")
element.click()

element = get_element_with_wait(element=driver, 
                XPATH="//iframe[@class = 'ag-popup__frame__layout__iframe']")
driver.switch_to.frame(element)

element = get_element_with_wait(element=driver, 
                XPATH="//input[@name = 'username']")
element.send_keys('study.ai_172')

element = get_element_with_wait(element=driver, 
                XPATH="//span[text() = 'Ввести пароль']/..")
element.click()

element = get_element_with_wait(element=driver, 
                XPATH="//input[@name = 'password']")
element.send_keys('NextPassword172#\n')

time.sleep(3)

mails = dict()
def get_date(stime):
    today = datetime.datetime.now()
    try:
        date = datetime.datetime.strptime(stime, '%d.%m.%y')
        day, month, year = date.day, date.month, date.year
    except ValueError:
        try:
            locale.setlocale(locale.LC_TIME, 'ru_RU')
            date = datetime.datetime.strptime(stime, '%d %b')
            day, month, year = date.day, date.month, today.year
            locale.setlocale(locale.LC_TIME, (None, None))
        except ValueError:
            return None
    
    return str(datetime.date(year, month, day))

def get_element_with_wait(element, XPATH):
    return WebDriverWait(element, 10).until( 
                EC.presence_of_element_located((By.XPATH, XPATH)))

are_mail_containers_ran_out = False

while not are_mail_containers_ran_out:
    are_mail_containers_load = False
    
    mail_containers = WebDriverWait(driver, 10).until( 
            EC.presence_of_all_elements_located((By.XPATH, 
            "//a[contains(@href, '/inbox/') and contains(@class, 'llc')]")))

    mails_size_before_add = len(mails)
    scan_counter = 0
    for a_tag_container in mail_containers:
        cur_link = a_tag_container.get_attribute("href")
        mails[cur_link] = {}
        sender_tag = get_element_with_wait(a_tag_container, 
                                ".//span[contains(@class, 'll-crpt')]")
        mails[cur_link]['sender'] = sender_tag.get_attribute("title")
        receive_date_tag = get_element_with_wait(a_tag_container, 
                                ".//div[contains(@class, 'llc__item_date')]")
        mails[cur_link]['receive_date'] = get_date(receive_date_tag.text)
        topic_tag = get_element_with_wait(a_tag_container, 
                                ".//span[contains(@class, 'll-sj__normal')]")
        mails[cur_link]['topic'] = topic_tag.text 

        scan_counter += 1

    if len(mails) == mails_size_before_add:
        are_mail_containers_ran_out = True 
            
    mail_containers[len(mail_containers)//2].send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)


for mail_link, content in mails.items():
    driver.get(mail_link)
    mail_body_tag = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'letter-body')]")))
    content['full_text'] = mail_body_tag.text
    driver.back()

# =================================================    
# Записываем даннуе в базу данных
# =================================================  
client = pymongo.MongoClient('localhost', 27017)
db = client.mails_db
db.drop_collection('mails_collection')
mails_collection = db.mails_collection

for mail_link, content in mails.items(): 
    mails_collection.update_one({"link": mail_link, **content}, {'$set': {"link": mail_link, **content}}, upsert=True) 

class Commands:
    RE_EXIT = re.compile(r"""(?P<command>(exit)|(quit)|(\\q))""", re.X)

message = """---Вывести все письма: all
---Вывести количество писем: count
---Вывести письма по отправителю: sender="наименование отправителя"
---Остановить работу: exit | quit | \q"""
print(message)
command = input("Введите команду: ").lower().strip()
while not Commands.RE_EXIT.search(command):
    if 'all' in command:
        for new in mails_collection.find({}):
            pprint(new)
    elif 'sender' in command:
        if command == 'sender':
            num = 0
            for sender in mails_collection.aggregate( [{"$group":{"_id": "$sender"}}]):
                num += 1
                print(f"{num}-{sender['_id']}")
        else:
            sender = command.replace("sender=", '')
            pattern = re.compile('sender', re.IGNORECASE)
            regex = bson.Regex.from_native(pattern)
            for mail in mails_collection.find({"sender": {"$regex": sender, "$options": "i"}}):
                pprint(mail)
    elif 'count' in command:
        pprint(mails_collection.count_documents({}))
    else:
        print("Команда не распознана")
        print(message)
    
    command = input("Введите команду: ")     


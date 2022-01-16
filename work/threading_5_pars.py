from cmath import pi
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

import random
import logging
import threading
import concurrent.futures
import time
import queue   

logging.basicConfig(filename='example.log', 
                    format='%(name)s %(levelname)s %(funcName)s %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8', 
                    level=logging.INFO)

class SafeDict(dict):

    def __init__(self, *args, **kwargs):
        self.message = 0
        self.get_lock = threading.Lock()
        self.set_lock = threading.Lock()
        # self.consumer_lock.acquire()
        super().__init__(*args, **kwargs)
    
    def __getitem__(self, item):
        self.set_lock.acquire()
        self.get_lock.acquire()
        value = super().__getitem__(item)
        self.get_lock.release()
        self.set_lock.release()
        return value

    def __setitem__(self, item, value):
        logging.info("%s:Зашли в setitem")
        self.set_lock.acquire()
        self.get_lock.acquire()
        logging.info("%s:Прошли через producer_lock.acquire()")
        super().__setitem__(item, value)

        self.set_lock.release()
        self.get_lock.release()
        logging.info("%s:Прошли через consumer_lock.release()")


my_dict = SafeDict()

def producer(pipeline, semaphore):
    """Pretend we're getting a message from the network."""
    semaphore.acquire()
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.put(message)
    
    logging.info("Producer reveived EXIT event. Exiting")
    semaphore.release()

class Consumer:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # открыть окно на весь экран
        # chrome_options.add_argument('start-maximized')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('prefs', {"profile.managed_default_content_settings.images": 2})
        # starts a new chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.implicitly_wait(10) # seconds

    
    def consumer(self, num, pipeline, semaphore):

        semaphore.acquire()
        # waiting_mess = True
        while not pipeline.empty():
            try:
                # time.sleep(0.001)
                url = pipeline.get(block=False)
                self.driver.get("https://mail.ru/")

                def get_element_with_wait(element, XPATH):
                    return WebDriverWait(element, 10).until( 
                        EC.presence_of_element_located((By.XPATH, XPATH)))

                
                self.driver.get(url)
                mail_body_tag = WebDriverWait(self.driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div")))
                logging.info(f"consumer {num} пытается записать данные в словарь")
                my_dict[url[0:40]] = mail_body_tag
            except queue.Empty:
                continue

            logging.info(f'Consumer {num} {url} (queue size={pipeline.qsize()})')

        logging.info(f"Consumer {num} received EXIT event. Exiting")
        semaphore.release()
        # pipeline.task_done()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = queue.Queue(maxsize=100)
    pipeline.put(r'https://news.mail.ru/politics/49626311/')
    pipeline.put(r'https://news.mail.ru/inregions/st_petersburg/91/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')
    pipeline.put(r'https://news.mail.ru/society/?utm_partner_id=945')



    event = threading.Event()
    semaphore = threading.Semaphore(10)
    
    # while not pipeline.empty():
    #     consumer(1, pipeline, semaphore)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # executor.submit(producer, pipeline, semaphore)   
        for num in range(2):
            worker = Consumer()
            executor.submit(worker.consumer, num, pipeline, semaphore)

    pass


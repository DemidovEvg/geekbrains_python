import bs4
import requests
import re
import argparse
import logging
import pathlib
import sys
import random
import transliterate

def main():
    parser()


def parser():
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',}

    source = { 'url': 'https://kakzovut.ru/man.html',
                'url_clean': 'https://kakzovut.ru',
                'out_class': {'class': 'vacancy-serp-item'},
                'vacancy_title': {'data-qa': 'vacancy-serp__vacancy-title'},
                'vacancy_compensation': {'data-qa': 'vacancy-serp__vacancy-compensation'},
                'vacancy_employer': {'data-qa': 'vacancy-serp__vacancy-employer'},
                'params':{'area': '2', 
                                'fromSearchLine': 'true',
                                'text': '',
                                'from': 'suggest_post',
                                'page': '0'}}


   
    response = requests.request('get', 
                                source['url'], 
                                headers=headers)
    print(response.url)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    names_class = soup.find_all(attrs={'class': 'nameslist'})
    result_set = []
    with open('names.txt', 'a', encoding='utf-8') as f:
        for vac in names_class:  
            names = vac.find_all('a')
            result_set.append(f"'{names[0].string}'")
            # name_translite = transliterate.translit(names[0].string, language_code='ru', reversed=True)
            # f.write(f'{name_translite} {random.randint(25,50)}\n')
        f.write(', '.join(result_set))

if (__name__)=="__main__":
    main()




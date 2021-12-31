import bs4
import requests
import re
import argparse
import logging
import pathlib
import sys


class Salary:
    def __init__(self, val, currency):
        self.__val = val
        self.__currency = currency

    @property
    def salary(self):
        return self.__val

    @salary.setter
    def salary(self, val):
        self.__val = val
        return self.__val

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    def __str__(self):
        return f'{self.__val} {self.__currency}'


def parser_hh_sj(work_position):
    log_file = pathlib.Path(__file__).parent / 'vacancy.log'
    # logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.warning)
    logging.basicConfig(encoding='utf-8', level=logging.INFO)
    def str_to_int(salary_str)->int:
        salary_list = []
        for sal in salary_str:
            if sal.isdigit():
                salary_list.append(sal)
        result = int(''.join(salary_list))
        if not result:
            return None
        else:
            return result

    def get_min_max_currency(salary_str)->dict:
        min_salary = Salary(None, None)
        max_salary = Salary(None, None)
        if not salary_str:
            return min_salary, max_salary
        if 'руб' in salary_str.lower():
            min_salary.currency = 'руб'
            max_salary.currency = 'руб'
        elif 'USD' in salary_str.lower():
            min_salary.currency = 'руб'
            max_salary.currency = 'руб'
        else:
            return min_salary, max_salary

        if 'от' in salary_str.lower():
            #Если попалю сюда, тогда это что-то такое "от  90 000   USD"
            min_salary.salary = str_to_int(salary_str)
        elif 'до' in salary_str.lower():
            #Если попалю сюда, тогда это что-то такое "до  90 000   USD"
            max_salary.salary = str_to_int(salary_str)
        elif re.search(r"['-'|'−'|'–'|'—']", salary_str):
            #Если попали сюда, тогда это что-то такое "100 000 — 110 000 руб."       
            if '-' in salary_str:
                delimiter = '-'
            elif '−' in salary_str:
                delimiter = '−'
            elif '–' in salary_str:
                delimiter = '–'
            elif '—' in salary_str:
                delimiter = '—'
            salaries = salary_str.split(delimiter)
            min_salary.salary = str_to_int(salaries[0])
            max_salary.salary = str_to_int(salaries[1])
        return min_salary, max_salary

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',}

    head_hunter = { 'url': 'https://spb.hh.ru/search/vacancy',
                    'url_clean': 'https://spb.hh.ru',
                    'common_container': {'class': 'vacancy-serp-item'},
                    'container_with_vacancy_title': {'data-qa': 'vacancy-serp__vacancy-title'},
                    'container_with_vacancy_compensation': {'data-qa': 'vacancy-serp__vacancy-compensation'},
                    'container_with_vacancy_employer': {'data-qa': 'vacancy-serp__vacancy-employer'},
                    'params':{'area': '2', 
                                'fromSearchLine': 'true',
                                'text': work_position,
                                'from': 'suggest_post',
                                'page': '0'}}

    superjob = {'url': 'https://spb.superjob.ru/vacancy/search',
                'url_clean': 'https://spb.superjob.ru',
                'common_container': 'f-test-search-result-item',
                'container_with_vacancy_title': {'class': '_6AfZ9'},
                'container_with_vacancy_compensation': {'class': 'f-test-text-company-item-salary'},
                'container_with_vacancy_employer': {'class': 'f-test-text-vacancy-item-company-name'},
                'params':{'keywords': work_position, 
                            'page': '0'}}

    vacancies = []

    for source in head_hunter, superjob:    
        page = 0
        vacancy_data = True
        while vacancy_data:
            source['params']['page'] = str(page) 
            page += 1 
            response = requests.request('get', 
                                        source['url'], 
                                        headers=headers, 
                                        params=source['params'])
            # print(response.url)
            soup = bs4.BeautifulSoup(response.text, features='html.parser')
            logging.info(f"current {source['url']=} {page=} with {source['container_with_vacancy_title']=}")
            vacancy_data = soup.find_all(attrs=source['common_container'])
            if not vacancy_data:
                break              
            for vac in vacancy_data:                
                try:       
                    vacancy_title_tag = vac.find(attrs=source['container_with_vacancy_title'])
                    vacancy_title = vacancy_title_tag.get_text()
                except (KeyError, AttributeError) as e:
                   logging.debug(f"Can't find element in {source['url']=} {page=} with {source['container_with_vacancy_title']=}")
                   continue

                try:
                    vacancy_compensation_raw = vac.find(attrs=source['container_with_vacancy_compensation']).get_text()        
                except (KeyError, AttributeError) as e:
                   logging.debug(f"Can't find element in {source['url']=} {page=} with {source['container_with_vacancy_compensation']=}")
                   vacancy_compensation_raw = None
                min_salary, max_salary = get_min_max_currency(vacancy_compensation_raw)
                
                try:
                    vacancy_href = vacancy_title_tag['href']
                except (KeyError, AttributeError) as e:
                   logging.debug(f"Can't find element in {source['url']=} {page=} with {'href'=}")
                   vacancy_href = None
                if vacancy_href and 'https' not in vacancy_href:
                    vacancy_href = source['url_clean'] + vacancy_href
                try:
                    vacancy_employer = vac.find(attrs=source['container_with_vacancy_employer']).get_text()
                except (KeyError, AttributeError) as e:
                   logging.debug(f"Can't find element in {source['url']=} {page=} with {source['container_with_vacancy_employer']=}")
                   vacancy_employer = None   
                
                vacancies += [{ 'title': vacancy_title,
                                'min salary': min_salary.salary,
                                'max salary': max_salary.salary,
                                'currency': min_salary.currency,
                                'emploer': vacancy_employer,
                                'link': vacancy_href }]
    return vacancies

def main():
    parser = argparse.ArgumentParser(description='script takes info about vacancy.')
    parser.add_argument('position', type=str, nargs='+', help='Enter position for search.\
        If there are several words, then use double quotes.')

    if len(sys.argv) > 1:
        user_input = parser.parse_args()
        work_position = ' '.join(user_input.position)
    else:
        while True:
            work_position = input('Введите должность для поиска: ')
            if work_position != '':
                break
    df = parser_hh_sj(work_position)
    file = pathlib.Path(__file__).parent / 'result.csv'
    df.to_csv(file)
    print(df)

if (__name__)=="__main__":
    main()




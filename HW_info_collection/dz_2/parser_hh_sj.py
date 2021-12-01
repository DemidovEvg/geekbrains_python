# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов Superjob и HH. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (отдельно минимальную и максимальную).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.
# Можно выполнить по желанию один любой вариант или оба при желании и возможности.

import bs4
import requests
import re
import argparse
import logging
import pathlib
import currency
import pandas
import sys

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


def parser_hh_sj(work_position):
    log_file = pathlib.Path(__file__).parent / 'vacancy.log'
    logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.INFO)

    def convert_to_float(salary_str):
        salary_list = []
        for i in salary_str:
            if i.isdigit() or i == '.' or i == ',':
                salary_list.append(i)
        result = None
        try:
            result = int(''.join(salary_list))
        except:
            logging.info(f"can't convert {salary_str} to int")
        return result

    def clean(salary_str):
        salary_list = []
        for i in salary_str:
            if i.isdigit() or i == '.' or i == ',' or i == '–' or i == '—':
                salary_list.append(i)
        result = ''.join(salary_list)
        return result

    def get_min_max_currency(salary_str)->dict:
        def min_max_currency_none():
            none_dict = {'min salary': '-', 
                        'max salary': '-',
                        'currency': '-'}
            return none_dict
        re.compile(r'^(?P<username>\w+)@(?P<domain>(?:\w+)(?:\.\w+)$)')
        min_max_currency = None
        is_rub = False
        if 'руб' in salary_str.lower():
            is_rub = True
            position_rub = salary_str.find('руб')
            salary_str = salary_str[:position_rub]
        else:
            position_usd = salary_str.upper().find('USD')
            salary_str = salary_str[:position_usd]

        if 'от' in salary_str.lower():
            #Если попалю сюда, тогда это что-то такое "от  90 000   USD"
            clean_salary_str = clean(salary_str)
            try:
                min_max_currency = {'min salary': convert_to_float(clean_salary_str),
                                    'max salary': '-',}
            except Exception:
                min_max_currency = min_max_currency_none()

        elif 'до' in salary_str.lower():
            #Если попалю сюда, тогда это что-то такое "до  90 000   USD"
            clean_salary_str = clean(salary_str)
            try:
                min_max_currency = {'min salary': '-',
                                    'max salary': convert_to_float(clean_salary_str),}
            except Exception:
                min_max_currency = min_max_currency_none()

        elif '–' in salary_str or '—' in salary_str:
            #Если попали сюда, тогда это что-то такое "100 000 — 110 000 руб."
            clean_salary_str = clean(salary_str)
            RE_MIN_MAX_CURRENCY = re.compile(r'''(?P<salary_min>\d+)[–|—]
                                (?P<salary_max>\d+)''', re.X)
            result = RE_MIN_MAX_CURRENCY.findall(clean_salary_str)
            try:
                min_max_currency = {'min salary': convert_to_float(result[0][0]),
                                    'max salary': convert_to_float(result[0][1]),}
            except Exception:
                min_max_currency = min_max_currency_none()
        else:
            min_max_currency = min_max_currency_none()

        usd_rub = currency.current_rates('USD')[0]
        min_max_currency['currency'] = 'USD'
        if is_rub:
            if min_max_currency['min salary'] != '-':
                min_max_currency['min salary'] = round(min_max_currency['min salary'] / usd_rub)
            if min_max_currency['max salary'] != '-':
                min_max_currency['max salary'] = round(min_max_currency['max salary'] / usd_rub)

        return min_max_currency

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',}

    head_hunter = { 'url': 'https://spb.hh.ru/search/vacancy',
                    'url_clean': 'https://spb.hh.ru',
                    'out_class': {'class': 'vacancy-serp-item'},
                    'vacancy_title': {'data-qa': 'vacancy-serp__vacancy-title'},
                    'vacancy_compensation': {'data-qa': 'vacancy-serp__vacancy-compensation'},
                    'vacancy_employer': {'data-qa': 'vacancy-serp__vacancy-employer'},
                    'params':{'area': '2', 
                                'fromSearchLine': 'true',
                                'text': work_position,
                                'from': 'suggest_post',
                                'page': '0'}}

    superjob = {'url': 'https://spb.superjob.ru/vacancy/search',
                'url_clean': 'https://spb.superjob.ru',
                'out_class': 'f-test-search-result-item',
                'vacancy_title': {'class': '_6AfZ9'},
                'vacancy_compensation': {'class': 'f-test-text-company-item-salary'},
                'vacancy_employer': {'class': 'f-test-text-vacancy-item-company-name'},
                'params':{'keywords': work_position, 
                            'page': '0'}}

    df = pandas.DataFrame(columns=('title', 
                                    'min salary', 
                                    'max salary', 
                                    'currency', 
                                    'emploer', 
                                    'link'))
    row = 0

    for source in head_hunter, superjob:
        for page in range(1):
            source['params']['page'] = str(page)
            #print(f"сайт - {source['url']} страница N - {source['params']['page']}")    
            response = requests.request('get', 
                                        source['url'], 
                                        headers=headers, 
                                        params=source['params'])
            print(response.url)
            soup = bs4.BeautifulSoup(response.text, features='html.parser')

            vacancy_data = soup.find_all(attrs=source['out_class'])
            
            for vac in vacancy_data:  
                def get_string_from_first_element(bs4_elements, attrs=None):
                    data = 'None'
                    if attrs != None:
                        try:
                            elements = bs4_elements.find_all(attrs=attrs)[0]
                            data = ''
                            for string in elements.strings:
                                data += string
                        except Exception:
                            logging.info(f"Can't find element with {attrs}")
                    return data

                def get_first_tag(bs4_elements, attrs=None):
                    data = bs4_elements
                    if attrs != None:
                        try:
                            data = bs4_elements.find_all(attrs=attrs)[0]
                        except Exception:
                            logging.info(f"Can't find element with {attrs}")
                    return data
                            
                
                vacancy_title = get_string_from_first_element(vac, 
                                attrs=source['vacancy_title'])
                if vacancy_title == 'None':
                    continue
                vacancy_compensation_raw = get_string_from_first_element(vac, 
                            attrs=source['vacancy_compensation'])
                vacancy_compensation = get_min_max_currency(vacancy_compensation_raw)
                vacancy_href = get_first_tag(vac, 
                                            attrs=source['vacancy_title'])['href']
                if 'https' not in vacancy_href:
                    vacancy_href = source['url_clean'] + vacancy_href

                vacancy_employer = get_string_from_first_element(vac, 
                                            attrs=source['vacancy_employer'])
                df.loc[row] = [vacancy_title, 
                                vacancy_compensation['min salary'], 
                                vacancy_compensation['max salary'],
                                vacancy_compensation['currency'],
                                vacancy_employer, 
                                vacancy_href]
                row += 1
    
    return df




if (__name__)=="__main__":
    main()




# 2.	Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) 
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
#  http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть 
#  содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат 
#  числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
#   Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. 
#   Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы 
#   доллара и евро.


#  Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# (Ответ) float приводит к утере точности print(0.1 + 0.1 + 0.1 == 0.3) => false

# 3.	*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, 
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, 
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

import requests
import decimal
import datetime

def current_rates(current_code, type_of_course):
    '''return course input currency with date


    '''
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    datetime_string = None
    for i in response.headers:
        if i == 'Date':
            date_time_string = response.headers[i].removesuffix(' GMT')
            datetime_object = datetime.datetime.strptime(date_time_string, '%a, %d %b %Y %H:%M:%S')
            datetime_string = datetime_object.strftime('%d.%m.%Y')
            
    #Что бы регистр не влиял на поиск => .upper()
    position_current_code = content.find(f'<CharCode>{current_code.upper()}</CharCode>', 0, len(content))
    if position_current_code != -1:
        position_course = content.find('<Value>', position_current_code, len(content)) + len('<Value>')
        position_course_end = content.find('</Value>', position_current_code, len(content))
        course_str = content[position_course:position_course_end].replace(',','.')
        result = type_of_course(course_str)
        return result, datetime_string
    else:
        return None, None, datetime_string
    
    
if __name__ == '__main__':
    current = 'usd'
    result, datetime_object = current_rates(current, decimal.Decimal)
    if result != None:
        print(f'Курс {current} равен {result:.4f}р /Дата ответа - {datetime_object}')
    else:
        print(f'None')
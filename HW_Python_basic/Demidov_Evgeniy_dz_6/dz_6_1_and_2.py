# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]


# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

import requests
import re
from time import perf_counter

url = f'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
start = perf_counter()
with requests.get(url, stream=True) as r:
    if r.encoding is None:
        r.encoding = 'utf-8'

    log_list = []
    #Определим что максимум можем занять 1 кб ОЗУ
    MAX_BYTES = 1024*30
    log_generator = r.iter_content(chunk_size = MAX_BYTES, decode_unicode=True)

    count = 0
    last_element = ''
    is_need_save_last_element = False
    previously_last_element = ''
    response_counter = dict()
    
    for log_chunk in log_generator:
        
        # Так как считываем информацию кусками, 
        # (начало куска)93.180.71.3 - - [17/May/204...
        # //93.180.71.3 - - [17/May/204...
        # //93.180.71.3 (кусок кончился без символа \n)
        # то необходимо добавить обрезок в конце, 
        # к первому элементу следующего куска
        if log_chunk[len(log_chunk)-1] != '\n':
             is_need_save_last_element = True
        else:
             is_need_save_last_element = False

        log_line_list = log_chunk.split('\n')
        log_line_list[0] = previously_last_element + log_line_list[0] 
        if is_need_save_last_element:
            previously_last_element = log_line_list[len(log_line_list) - 1]
            log_line_list[len(log_line_list) - 1] = ''
        else:
            previously_last_element = ''
                 
        for line in  log_line_list:
            count = count + 1
            is_find_remote_addr = False
            is_find_request_type = False
            is_requested_resource = False
            for log_element in line.split():
                if not is_find_remote_addr:
                    remote_addr = re.search(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', log_element)

                    if remote_addr:
                        is_find_remote_addr = True
                if is_find_remote_addr and not is_find_request_type:   
                    request_type = re.search(r'(?:GET)|(?:PUT)|(?:CONNECT)|(?:DELETE)|(?:HEAD)|(?:OPTIONS)|(?:POST)|(?:TRACE)', 
                                            log_element, flags=re.IGNORECASE)
                    if request_type:
                        is_find_request_type = True
                if is_find_request_type and not is_requested_resource:
                    requested_resource = re.search(r'^(?:/\w+){1,10}\w+$', log_element)
                    if requested_resource:
                        is_requested_resource = True
                if is_find_remote_addr and is_find_request_type and is_requested_resource:
                    log_list.append((remote_addr.group(0), request_type.group(0), requested_resource.group(0)))
                    if remote_addr.group(0) in response_counter:
                        response_counter[remote_addr.group(0)] += 1
                    else:
                        response_counter[remote_addr.group(0)] = 1
                    break
        

        
print(f'get data time: {perf_counter() - start}') 
print(f'Length log list: {len(log_list)}')

spammers = list()
# Пусть спаммеры - это те у кого больше 1000 запросов
for current_ip_iter,  current_ip_requests_count_iter in response_counter.items():
    if current_ip_requests_count_iter > 1000:
        spammers.append((current_ip_iter, current_ip_requests_count_iter))

# Отсортируем спамеров по убыванию запросов
spammers_sorted_list = sorted(spammers, key = lambda a: a[1], reverse=True)

place = 1
for spammer_ip_iter, spammer_requests_count_iter  in spammers_sorted_list:
    print(f'The {place}th spammer is {spammer_ip_iter} with {spammer_requests_count_iter} requests')
    place += 1

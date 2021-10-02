# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import requests
import re
from pathlib import Path
import csv

url = r'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

file = Path(__file__).parent/'parse_raws.csv'
#print(file)
count = 0
qwe =  requests.get(url, stream=True)
print(qwe)
with requests.get(url, stream=True) as r,  file.open('w', newline='') as fp:
    file_writer = csv.writer(fp)
    #Определим что максимум можем занять 30 кб ОЗУ
    MAX_BYTES = 1024*30
    log_generator = r.iter_content(chunk_size = MAX_BYTES, decode_unicode=True)

    last_element = ''
    is_need_save_last_element = False
    previously_last_element = ''
    response_counter = dict()

    RE_RESPONSE = re.compile(r'''^(?P<remote_addr>\d+(?:[\.|:]\d+)+).+
                        (?P<request_datetime>\[.+\])\s+"
                        (?P<reguest_type>\w+)\s+
                        (?P<request_resource>[\w|\/|\.]+)\s+HTTP\/[\d|\.]+\"\s+
                        (?P<response_code>\d+)\s+
                        (?P<response_size>\d+).+$''', re.X)

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
            count += 1
            result = RE_RESPONSE.findall(line)
            if result:
                file_writer.writerow(result[0])
            elif line.strip() != '':
                file_writer.writerow(['error_read'])


            


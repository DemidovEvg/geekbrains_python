# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные вакансии в созданную БД.
# 3) Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.

# Реализованно в цикле в проверке if not db[work_position].count_documents({uniq_key: new_v[uniq_key]}, limit = 1):

import pymongo
import pprint
import time
import sys
import pathlib
path_to_dz2 = pathlib.Path(__file__).parent.parent / 'dz_2'
sys.path.append(str(path_to_dz2))
import parser_hh_sj
import uuid
import bson
import argparse


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
work_position = work_position.lower()
df = parser_hh_sj.parser_hh_sj(work_position)

dict_vacancy = df.to_dict('records')

client = pymongo.MongoClient('localhost', 27017)
db = client['vacancy_database']
collection = db[work_position]
print(db.list_collection_names())
append = 0
start = time.perf_counter()
for new_v in dict_vacancy:
    uniq_key = 'link'
    if not db[work_position].count_documents({uniq_key: new_v[uniq_key]}, limit = 1):
        append += 1
        try:
            db[work_position].insert_one(new_v)
        except:
            print(f'!!!!!!!!!!!{new_v}')

print(f"Append time with index when adding one by one is equal = \
{time.perf_counter() - start}, append = {append}, all num = {len(dict_vacancy)}")


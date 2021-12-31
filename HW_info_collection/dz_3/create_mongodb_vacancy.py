# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB 
# и реализовать функцию, которая будет добавлять только новые вакансии/продукты в вашу базу.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии 
# с заработной платой больше введённой суммы (необходимо анализировать оба поля зарплаты).
#  Для тех, кто выполнил задание с Росконтролем - напишите запрос для поиска продуктов 
# с рейтингом не ниже введенного или качеством не ниже введенного 
# (то есть цифра вводится одна, а запрос проверяет оба поля)

import sys
from pymongo import MongoClient
from pprint import pprint
import re
import hashlib
import pymongo

import parser_hh_sj


class Vacancies:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.vacancy_db
        self.vacancy_collection = self.db.vacancy_collection

    def clean_db(self):
        self.vacancy_collection.delete_many({})

    def update(self, vacancy_name):
        vacancies = parser_hh_sj.parser_hh_sj(vacancy_name)
        counter = 0 
        for vacancy in vacancies:
            hexdigits = hashlib.md5(vacancy['link'].encode()).hexdigest()
            maxsize_8_bytes = 2**63 - 1
            vacancy["_id"] = int(hexdigits, 16) % maxsize_8_bytes
            try:
                self.vacancy_collection.insert_one(vacancy)  
                counter += 1
            except pymongo.errors.DuplicateKeyError:
                pass    
        if counter % 10 == 1 and counter != 11:
            ends = {'нов': 'ая', 'ваканс': 'ия'}
        elif counter % 10 in [2, 3, 4] and counter not in [12, 13, 14]:
            ends = {'нов': 'ые', 'ваканс': 'ии'}
        else:
            ends = {'нов': 'ых', 'ваканс': 'ий'}
        print(f"Добавлено {counter} нов{ends['нов']} ваканс{ends['ваканс']}")

    def filter(self, vacancy_name=None, min_salary=None, max_salary=None):
        conditions = []
        if vacancy_name:
            conditions += [{"title": { "$regex": vacancy_name, "$options": 'i'}}]
        if min_salary:
            conditions += [{"$or": [{"min salary":{"$gte": min_salary}}, {"max salary":{"$gte": min_salary}}]}]
        if max_salary:
            conditions += [{"max salary":{"$lte": max_salary}}]
        if conditions:
            return self.vacancy_collection.find({"$and":conditions})
        else:
            return self.vacancy_collection.find({})
    
    def count(self, vacancy_name=None):
        if vacancy_name:
            return self.vacancy_collection.count_documents({"title": { "$regex": vacancy_name, "$options": 'i'}})
        else:
            return self.vacancy_collection.count_documents({})

    def drop(self):
        self.vacancy_collection.drop()       
       
class Commands:
    RE_SEARCH = re.compile(
        r"""(?P<command>search)\s+
        (?P<vacancy_name>(\w+)|(["|'][^"]+["|']))
        (\s+(min=)(?P<min_salary>\d+)){0,1}
        (\s+(max=)(?P<max_salary>\d+)){0,1}""", re.X)
    RE_RELOAD_OR_NEW = re.compile(
        r"""(?P<command>(new)|(reload))\s+
        (?P<vacancy_name>(\w+)|(["|'][^"]+["|']))""", re.X)
    RE_COUNT = re.compile(
        r"""(?P<command>count)(\s+(?P<vacancy_name>(\w+)|(["|'][^"]+["|']))){0,1}""", re.X)
    RE_EXIT = re.compile(
        r"""(?P<command>(exit)|(quit)|(\\q))""", re.X)


def main():
    vacancies  = Vacancies()
    # for i in vacancies.filter(vacancy_name=None, min=None, max=None):
    #     pprint(i)

    message = """---Получить списко команд: -h | help
---Найти переданную вакансию в бд: search ("название вакансии"|all) [min=...] [max=...]
---Обновить данные по вакансии в бд: reload "название вакансии"
---Получить данные по вакансии в бд: new "название вакансии"
---Получить количество вакансий в бд: count ("название вакансии"|all)
---Очистить коллекцию: drop
---Остановить работу: exit | quit | \q"""
    print(message)
    command = input("Введите команду: ").lower()
    while not Commands.RE_EXIT.search(command):
        if '-h' in command or 'help' in command:
            print(message)
        elif 'search' in command:
            command_parts = Commands.RE_SEARCH.search(command)
            if 'all' in command_parts['vacancy_name']:
                vacancy_name = None
            else:
                vacancy_name = command_parts['vacancy_name']
            if command_parts['min_salary']:
                min_salary = int(command_parts['min_salary'])
            else:
                min_salary = None
            if command_parts['max_salary']:
                max_salary = int(command_parts['max_salary'])
            else:
                 max_salary = None

            result = vacancies.filter(vacancy_name=vacancy_name, 
                                    min_salary=min_salary, 
                                    max_salary=max_salary)
            for i in result:
                pprint(i)
        elif 'reload' in command or 'new' in command:
            command_parts = Commands.RE_RELOAD_OR_NEW.search(command)
            vacancy_name = command_parts['vacancy_name']
            vacancies.update(vacancy_name)
        elif 'count' in command:
            command_parts = Commands.RE_COUNT.search(command)
            vacancy_name = command_parts['vacancy_name']
            print(f"Всего {vacancies.count(vacancy_name)} документов")
        elif 'erase' in command:
            vacancies.drop()
        else:
            print("Команда не распознана")
            print(message)
        command = input("Введите команду: ")     


if __name__ == "__main__":
    main()

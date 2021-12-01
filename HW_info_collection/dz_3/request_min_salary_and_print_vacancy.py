# 2)Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.


import pymongo
import pprint


client = pymongo.MongoClient('localhost', 27017)
# print(client.list_database_names())
db = client['vacancy_database']
# print(db.list_collection_names())
# print(db['vacancy'].find_one())
wish_position = input("Enter position you want: ")
work_position = wish_position.lower()
if wish_position not in db.list_collection_names():
    raise ValueError("Base don't have this vacancy")

try:
    wish_salary = int(input("Enter minimum salary you want: "))
except Exception:
    print("You enter wrong salary. Enter valid number.")

pp = pprint.PrettyPrinter(indent=3)

print('Vacancy list exactly for you:')
for vac in db[wish_position].find({'max salary': {'$gt': wish_salary}}):
    pp.pprint(vac)
print('='*30)
print('Vacancy list may be for you:')
for vac in db[wish_position].find({'max salary': '-'}):
    pp.pprint(vac)
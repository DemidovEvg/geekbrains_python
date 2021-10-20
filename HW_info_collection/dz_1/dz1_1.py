# Посмотреть документацию к API GitHub, разобраться как вывести список 
# репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.


import requests
import json
import pathlib

name = "DemidovEvg"
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json',
            'Authorization': 'token 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'}

req = requests.get(f'https://api.github.com/users/{name}/repos')

data = req.json()
result_dict = {}
count = 0
for dict_ in data:
    if 'name' in dict_:
        result_dict[f'repo_{count}'] = dict_['name']
        print(f'repo_{count}: {dict_["name"]}')
        count += 1


file = pathlib.Path(__file__).parent/'Demidov_repos.json'
print(file)
with file.open('w', encoding='utf-8') as fp:
    json.dump(result_dict, fp, indent=3)

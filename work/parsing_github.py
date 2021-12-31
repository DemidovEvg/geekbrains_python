# Посмотреть документацию к API GitHub, разобраться как вывести список 
# репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json
import pathlib
from pprint import pprint
import os

name = "DemidovEvg"
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json',
            'Authorization': 'token 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'}

req = requests.get(f'https://api.github.com/users/{name}/repos')

print(f'List of repos for {name}')
print([rs[r] for rs in req.json() for r in rs if r == 'name'])

file = pathlib.Path(__file__).parent/'Demidov_repos.json'
print(file)
with file.open('w', encoding='utf-8') as fp:
    json.dump(req.json(), fp, indent=3)

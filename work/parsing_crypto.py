# Изучить список открытых API. Найти среди них любое, требующее авторизацию 
# (любого типа). Выполнить запросы к нему, пройдя авторизацию.
#  Ответ сервера записать в файл.

import requests
from pprint import pprint
import pathlib
import json

apikey = "53OU5EWW6XB896AF"

parameters = []
parameters.append('function=DIGITAL_CURRENCY_MONTHLY')
parameters.append('symbol=ETH')
parameters.append('market=USD')
parameters.append('apikey=53OU5EWW6XB896AF')

url = f'https://www.alphavantage.co/query?{"&".join(parameters)}'
print(url)
r = requests.get(url)
meta_data = r.json()
eth_in_usd = {}
eth_in_usd['ETH'] = {}
data = meta_data['Time Series (Digital Currency Monthly)']

for date, currencies in data.items():
    for cur, val in currencies.items():
        if 'open (USD)' in cur:
           eth_in_usd['ETH'][date] = val
           break

pprint(eth_in_usd)

file = pathlib.Path(__file__).parent/'ETH_quotes_months.json'
with file.open('w', encoding='utf-8') as fp:
    json.dump(eth_in_usd, fp, indent=3)

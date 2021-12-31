import requests
import json
import pathlib
from pprint import pprint
import os

name = "DemidovEvg"
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': '*/*',}

url = "https://yandex.ru"
response = requests.get(url, headers=headers)

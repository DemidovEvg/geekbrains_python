from pprint import pprint
from lxml import html
import requests
import pathlib

path = pathlib.Path(__file__).parent / 'test.html'
content = path.open('r').read()
root = html.fromstring(content)

films = root.xpath("//*")

print(films)





# main_link = 'https://www.kinopoisk.ru'
# url = main_link+'/afisha/new/city/2/'
# response = requests.get(url)
# print(url)
# root = html.fromstring(response.text)
# films = root.xpath("//div[@class='item']")

# for film in films:
#     href = film.xpath(".//div[@class='name']/a/@href")
#     name = film.xpath(".//div[@class='name']/a/text()")
#     genre = film.xpath('.//div[@class="gray"][last()]/text()')[2].replace(' ','')
#     root = html.fromstring(response.text)
#     result = root.xpath("//a[contains(@class,'link_cropped_no')]/@href | //a[contains(@class,'organic__url_type_multiline')]/@href")
#     rating = film.xpath('.//div[@class="rating"]/span/text()')
#     print(name, href, rating, genre)
import requests
import xml.etree.ElementTree as ET
import decimal
import datetime

def current_rates(current_code, type_of_course=decimal.Decimal):
    '''return course input currency with date
    '''
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    datetime_string = None
    for i in response.headers:
        if i == 'Date':
            date_time_string = response.headers[i].removesuffix(' GMT')
            datetime_object = datetime.datetime.strptime(date_time_string, '%a, %d %b %Y %H:%M:%S')
            datetime_string = datetime_object.strftime('%d.%m.%Y')
            
    root = ET.fromstring(content)
    current_code = current_code.upper()
    try:
        valute_list = root.findall(f"*[CharCode='{current_code}']")
        valute_tag = valute_list[0]
        course_tag = valute_tag.findall(".//Value")
        course_str = course_tag[0].text.replace(',', '.')
        course = type_of_course(course_str)
        return course, datetime_string
    except Exception:
        return None, datetime_string
    
if __name__ == '__main__':
    current = 'eur'
    result, datetime_object = current_rates(current, float)
    if result != None:
        print(f'Курс {current} равен {result:.4f}р /Дата ответа - {datetime_object}')
    else:
        print(f'None')
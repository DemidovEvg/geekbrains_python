# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import datetime


class Date:
    date = None
    def __init__(self, date):
        Date.date = date

    
    @classmethod
    @property
    def date_parse_simple(cls):
        try:
            day, month, year = (int(d) for d in cls.date.split('-'))
        except ValueError as e:
            print(e)
            raise e
        else:
            return (day, month, year)

    @classmethod
    @property
    def  date_parse_hard(cls):
        try:
            date = datetime.datetime.strptime(cls.date, f'%d-%m-%Y')
        except ValueError as e:
            print(e)
            raise e
        else:
            return (date.day, date.month, date.year)

    @staticmethod
    def date_validation(day, month, year):
        try:
            datetime.date(year, month, day)   
        except ValueError as e:
            print(e)
            raise e
        else:
            print('Date is correct!')


             
d = Date('301-10-2021')
parse = Date.date_parse_simple
print(parse)
Date.date_validation(*parse)
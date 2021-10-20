# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re

def email_parse(email):
    RE_EMAIL = re.compile(r'^(?P<username>\w+)@(?P<domain>(?:\w+)(?:\.\w+)$)')
    #RE_EMAIL = re.compile(r'.+')
    email_parts = RE_EMAIL.findall(email)
    
    if email_parts:
        username = email_parts[0][RE_EMAIL.groupindex['username']-1]
        domain = email_parts[0][RE_EMAIL.groupindex['domain']-1]
        return {'username':username, 'domain':domain}
    else:
        raise ValueError(f"Email {email} is\'t valid email")

email_1 = 'username@qwe.ru'
print(email_parse(email_1))

email_1 = 'someone@geekbrainsru'
print(email_parse(email_1))



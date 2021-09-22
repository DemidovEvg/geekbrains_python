# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html


# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
from pathlib import Path

script_dir = os.path.dirname(__file__)
starter = os.path.join(script_dir, 'starter2.yaml')
paths = []

with open(starter, 'r') as fp:
    count_space_previously = 0
    count_space_curent = 0
    path_list = []
    cur_dir = Path('')
    for el in fp:
        if "#" not in el:
            if ':' in el: #значит не конец пути
                count_space_curent = (len(el) - len(el.lstrip(' ')))//3
                if count_space_previously > count_space_curent:
                    for i in range(count_space_curent, count_space_previously + 1):
                        path_list[i] = ''
                el = el.replace(':','').replace('-','').strip()

                if len(path_list)<=count_space_curent:
                    path_list.append(el)
                else:
                    path_list[count_space_curent] = el
                cur_dir = Path(script_dir, *path_list)

            else:
                count_space_previously = (len(el) - len(el.lstrip(' ')))//3 - 1
                el = el.replace('-','').strip()
                cur_dir = Path(cur_dir, el)
                if not cur_dir.exists():
                    if cur_dir.suffix == '':
                        try:
                            cur_dir.mkdir(parents=True, exist_ok=True)
                        except Exception as e:
                            print('Incorrect name folder in starter2.yaml')
                            print(e)
                    else:
                        try:
                            cur_dir.parent.mkdir(parents=True, exist_ok=True)
                            with cur_dir.open("w") as fp:
                                pass
                        except Exception as e:
                            print('Incorrect name file in starter2.yaml')
                            print(e)
                cur_dir = cur_dir.parent    
                    
                

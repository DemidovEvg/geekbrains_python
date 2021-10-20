# 1) Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


# 2) #url1 Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); #url2 как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os
import csv

script_dir = os.path.dirname(__file__)
starter = os.path.join(script_dir, 'starter.csv')
paths = []
with open(starter, 'r') as fp:
    starter_iter = csv.reader(fp)
    for el in starter_iter:
        paths.append(os.path.join(script_dir,*el))
    

for file_or_folder in paths:
    
        if not os.path.exists(file_or_folder):
            if len(file_or_folder.split('.')) > 1:
                try:
                    with open(file_or_folder, 'w') as fp:
                        pass
                except Exception as e:
                    print(e)
                    pass
            else:
                try:
                    os.makedirs(file_or_folder)
                except Exception as e:
                    print(e)
                    pass
        


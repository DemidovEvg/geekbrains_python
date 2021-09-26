# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html


# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.


import os
import shutil
from pathlib import Path
from collections import defaultdict
from os.path import relpath


script_dir = Path(__file__).parent
root_dir = script_dir/'dem_project'

django_files = defaultdict(list)
folder_with_templates = Path(script_dir, 'templates_set')

if not folder_with_templates.exists():
    folder_with_templates.mkdir()
    
for template_folder in root_dir.glob(r'**\templates'):
    for template_file in template_folder.glob(r'**\*.*'):
        #print(template_file)  
        rel_path_file = template_file.relative_to(template_folder)
        new_path_file = folder_with_templates / rel_path_file
        print(new_path_file)
        new_path_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(template_file, new_path_file)


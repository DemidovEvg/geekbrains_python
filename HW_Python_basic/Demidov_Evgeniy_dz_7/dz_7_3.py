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
    
for root, dirs, files in os.walk(root_dir.resolve()):
    if 'templates' in root:
        for f in files:
            f_path = os.path.join(root, f)
            rel_path = os.path.relpath(f_path, root_dir)
            f_output_path = os.path.join(folder_with_templates, rel_path)
            path_for_file = Path(f_output_path).parent
            path_for_file.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f_path, f_output_path)


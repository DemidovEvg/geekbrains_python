1.	Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
====================================
Решение:
dz_7_1.py - скрипт решения
starter.csv - файл в папке где и скрипт, содержит пути и файлы для создания
Структура создается в той же папке где лежит скрипт
====================================
2.	*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
===================================
Решение:
dz_7_2.py - скрипт решения
starter2.yaml - файл в папке где и скрипт, содержит пути и файлы для создания
При заполении файла starter2.yaml необходимо следовать строго указанным правилам, которые описаны в комментариях в нем. Это сделано для упрощения обработки данных, иначе логика начинает усложнятся.
Структура создается в той же папке где лежит скрипт
===================================
3.	Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
===================================
Решение:
dz_7_3.py - скрипт решения
Структура получается из скрипта dz_7_2.py.
Сборка шаблонов осуществяется в папку templates_set, которая находится в той же папке где и скрипт
Структура в которой лежат файлы шаблонов, повторяет исходную.
===================================

4.	Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
===================================
Решение:
dz_7_4.py - скрипт решения
Информацию собираем из текущей рабочей директории
===================================

5.	*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
===================================
Решение:
dz_7_5.py - скрипт решения
Информацию собираем из текущей рабочей директории
===================================

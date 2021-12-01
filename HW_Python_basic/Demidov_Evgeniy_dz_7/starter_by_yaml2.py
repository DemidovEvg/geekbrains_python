import os

curent_folder = os.path.dirname(__file__)

with open(os.path.join(curent_folder, 'config.yaml'), 'r', encoding = 'utf-8') as f:
    starter = f.read().replace('|','').replace('-',' ')
print()


first_step = True
level_spaces = {}
level_path = {}
for line in starter.splitlines() + ['stopline']:
    if line.strip()[0] == "#" or line.strip() == '':
        continue
    clean_line = line.lstrip()
    if first_step:
        curlevel = 1  
        previous_spaces = len(line) - len(clean_line)
        level_spaces[1] = previous_spaces
        level_path[1] = line
        # print(line)
        # print(previous_spaces)
        first_step = False
        continue
    spaces = len(line) - len(clean_line)
    # print(line)
    # print(spaces)


    def create_folder_or_file(path_list):
        curpath = os.path.join(curent_folder, os.path.join(*path_list))
        if not os.path.exists(curpath):
            if len(curpath.rsplit('.', maxsplit=1)) > 1:          
                path_to_file = os.path.dirname(curpath)
                file_name = os.path.basename(curpath)
                print(f'Создаю файл: {file_name} по пути {path_to_file}')
                if not os.path.isdir(path_to_file):
                    os.makedirs(path_to_file)
                open(curpath, 'w', encoding='utf-8').close()
            else:
                print(f'Создаю папку: {curpath}')
                os.makedirs(curpath)


    if spaces == previous_spaces or line == 'stopline':
        create_folder_or_file([str(i) for i in level_path.values()])   
        previous_spaces = spaces
        level_spaces[curlevel] = spaces
        level_path[curlevel] = clean_line
    elif spaces > previous_spaces:
        curlevel += 1
        previous_spaces = spaces
        level_spaces[curlevel] = spaces
        level_path[curlevel] = clean_line
    else: 
        create_folder_or_file([str(i) for i in level_path.values()])   
        ls_copy = dict(level_spaces)
        curlevel = 1
        previous_spaces = spaces
        for key, val in reversed(ls_copy.items()):
            if spaces > val:
                curlevel = key + 1             
                break
            else:
                level_spaces.popitem()  
                level_path.popitem()  
        previous_spaces = spaces   
        level_spaces[curlevel] = spaces
        level_path[curlevel] = clean_line
    

        



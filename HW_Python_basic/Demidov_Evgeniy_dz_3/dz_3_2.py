# Подумайте: полезен ли будет вам оператор распаковки? //Да
# Как поступить, если потребуется сортировка по ключам? //sorted(result_dict)
# Можно ли использовать словарь в этом случае? //Только преобразовав в последовательности, например список

def thesaurus_adv(*args):
    ''' Return dictionary sort with first surname and name letter 


        Result lool like С : {'А': ['Анна Савельева'], 'И': ['Иван Сергеев', 'Инна Серова']}
        Result sorted by first letter in surname
    '''
    name_and_surname_list = [*args]

    def dict_first_letter_name(name_and_surname_list):
        set_of_the_first_letter_in_names = set(map(lambda n: n[0], name_and_surname_list ))
        name_and_surname_dict_inner = dict()
        for first_letter_in_name in set_of_the_first_letter_in_names:
            name_and_surname_dict_inner[first_letter_in_name] = []
            for name_and_surname in name_and_surname_list :
                if name_and_surname[0] == first_letter_in_name:
                    name_and_surname_dict_inner[first_letter_in_name].append(name_and_surname)
        return name_and_surname_dict_inner
    
    set_of_the_first_letter_in_surname = set(map(lambda n: n.split(' ')[1][0], name_and_surname_list))
    name_and_surname_dict_outer = dict()
    for first_letter_in_surname in set_of_the_first_letter_in_surname:
        selected_surname_list = []
        for n in name_and_surname_list:
            if n.split(' ')[1][0] == first_letter_in_surname:
                selected_surname_list.append(n)

        name_and_surname_dict_outer[first_letter_in_surname] = dict_first_letter_name(selected_surname_list)

    return  name_and_surname_dict_outer


if (__name__) == '__main__':

    result_dict = thesaurus_adv("Алексей Мордашов", "Владимир Потанин", "Владимир Лисин", "Вагит Алекперов", 
                            "Леонид Михельсон", 'Геннадий Тимченко', 'Алишер Усманов', 'Андрей Мельниченко', 
                            'Павел Дуров', 'Сулейман Керимов')

    for surname_key in sorted(result_dict):
        print(f"{surname_key: >1} : ")

        for name_key in sorted(result_dict[surname_key]):
            print(f"{name_key: >5} : {result_dict[surname_key][name_key]}")

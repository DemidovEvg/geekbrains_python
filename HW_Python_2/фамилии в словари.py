from codecs import encode
import json

def thesaurus(*args):
    names_dict = {}
    for el in args:
        first_letter = el[0].upper()
        if first_letter not in names_dict:
            names_dict[first_letter] = [el]
        else:
            if el not in names_dict[first_letter]:
                names_dict[first_letter].append(el)
    return names_dict

def thesaurus_adv(*args):
    last_first_names_dict = {}
    for el in args:
        fname, lname = el.split(' ')
        f_first_letter, l_first_letter = fname[0], lname[0]
        if l_first_letter not in last_first_names_dict:
            last_first_names_dict[l_first_letter] = {f_first_letter: [el]}
        elif f_first_letter not in last_first_names_dict[l_first_letter]:
            last_first_names_dict[l_first_letter].update({f_first_letter: [el]})
        else:
            if el not in last_first_names_dict[l_first_letter][f_first_letter]:
                last_first_names_dict[l_first_letter][f_first_letter].append(el)
    return last_first_names_dict
        

a = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(a)



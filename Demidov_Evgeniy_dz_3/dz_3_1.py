num_translate_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

def num_translate_adv(num_string):
    '''translate numeral from 1 to 10 into russian
    
    
        You can enter capitalize numeral
    '''
    if num_string.lower() in num_translate_dict:
        if num_string[0].istitle():
            return num_translate_dict[num_string.lower()].capitalize()
        else:
            return num_translate_dict[num_string]
        
    else:
        return None


if (__name__) == '__main__':
    print(num_translate_adv('ten'))


# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]


# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое 
# слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choices, sample


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num=1, *, with_repeat=False)->list:
    '''Return N funny jokes

        
        If with_repeat = False number jokes has limit 5
    '''
    jokes_list = []
    sample_or_choice = None
    if not with_repeat and num <= len(nouns) and num <= len(adverbs) and num <= len(adjectives):
        sample_or_choice = sample
    elif with_repeat:
        sample_or_choice = choices
    else:
        raise ValueError('You want to much unique jokes')
    
    for noun, adverb, adjective in zip(sample_or_choice(nouns, k=num), sample_or_choice(adverbs, k=num), sample_or_choice(adjectives, k=num)):
        jokes_list.append(f'{noun} {adverb} {adjective}')

    return jokes_list


if (__name__) == '__main__':
    jokes = get_jokes(10, with_repeat=True)
    print(jokes)
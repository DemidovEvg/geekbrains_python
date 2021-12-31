while True:
    counter = int(input())
    if counter % 10 == 1 and counter != 11:
        words = {'нов': 'ая', 'ваканс': 'ия'}
    elif counter % 10 in [2, 3, 4] and counter not in [12, 13, 14]:
        words = {'нов': 'ые', 'ваканс': 'ии'}
    else:
        words = {'нов': 'ых', 'ваканс': 'ий'}
    print(f"Добавлено {counter} нов{words['нов']} ваканс{words['ваканс']}")
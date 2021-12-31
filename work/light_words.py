def foo(s):
    """ 
    Вначале делим строку на список кортежей, 
    [(смежная левая часть, часть для анализа, правая смежная часть)]
    а далее логика следующая, 
    1) для трех и более нулей количество изменений равно остатку от деления на 3, 
    при этом крайние символы никогда не меняется, поэтому смежные части можно не анализировать

    2) для двух и более единиц количество изменений равно остатку от деления на 2,
    при этом когда количество единиц четное, то необходимо анализировать левую и правую
    смежную часть, так как либо там, либо там появляется новый символ
    """
    # заменим гласные на 1, согласные на 0 для удобства
    s_with_one_and_zero = []
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            s_with_one_and_zero.append('1')
        else:
            s_with_one_and_zero.append('0')
    s_with_one_and_zero.append('')
    piece = [s_with_one_and_zero[0]]
    parts = []

    for i in range(1, len(s_with_one_and_zero)): 
        if piece[0] == s_with_one_and_zero[i]:
            piece.append(s_with_one_and_zero[i]) 
        else:
            parts.append(piece)
            piece = [s_with_one_and_zero[i]]

    left = ['']
    left_body_right = []

    for i in range(len(parts)):
        if i < len(parts) - 1:
            right = parts[i+1]
        else:
            right = ['']
        left_body_right.append( (left, parts[i], right) )
        left = parts[i]

    change_count = 0
    for left, body, right in left_body_right:
        if body[0:2] == ['1', '1']:
            change_count += len(body)//2
            if left != '':
                possible_change_left_delta = len(left)//3 - (len(left)+1)//3
            else:
                possible_change_left_delta = 0
            
            if right != '':
                possible_change_right_delta = len(right)//3 - (len(right)+1)//3
            else:
                possible_change_right_delta = 0

            if (possible_change_left_delta == 1 and
                 possible_change_left_delta == possible_change_right_delta):
                change_count += 1
        elif body[0:3] == ['0', '0', '0']:
            change_count += len(body)//3
    return change_count

print(foo('ieuzzz'))

expression = '15*3', '15/3', '15//3', '15**3'

for exp in expression:
    print(f'type({exp:^5}) = {eval(exp):<5} - {type(eval(exp))}')

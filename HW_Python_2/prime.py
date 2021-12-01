
def validation(element, *args):
    result = element
    for val in args:
        try:
            result = val(result)
        except Exception as e:
            raise e
    return result

def greater_than_two(x):
    if x > 2:
        return x
    else:
        raise ValueError('Value equal or less than two')

def prime(x):
    y = x // 2
    while y > 1:
        if x % y == 0:
            raise ValueError('Not prime')
        y -= 1
    else:
        return x

y = None
try:
    y = validation( input(), 
                    int, 
                    greater_than_two,
                    prime)
    print(f'All validation done')
except Exception as e:
    print(e)
    raise e



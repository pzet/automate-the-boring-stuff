spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    if len(list) == 1:
        return list[0]
    else:
        return '{} and {}'.format(', '.join(list[:-1]), list[-1])

print(comma_code(spam))

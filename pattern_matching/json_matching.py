def parse_response(value):
    match value:
        case {'key': 1000, **rest}:
            return rest['id']
        case ('error', message) | ('error', message, *_):
             raise ValueError(message)
        case {'meta': val, **rest} if not rest:
            return val['id']
        case {'meta': {'code': _, 'error': error}, 'info': [{'allowed': allowed}, _]}:
            return f'{error}, {allowed}'
        case (set() as x, _) if len(x) == 2: # первая часть вырожения - это прверка на множество и присвоение ему псевдонима х,
                                             # вторая часть - это проверка, чтобы тип данных хранил в себе два элемента
            return max(x)
        case _: # wildcard
            raise ValueError(f'Unknown value: {value}')


if __name__ == '__main__':
    first = {'key': 1000, 'id': 999}
    second = ['error', 'Slow network connection']
    third = {'meta': {'id': 999}}
    fourth = {'meta': {'code': 200, 'error': 'no'}, 'info': [{'allowed': 'yes'}, 111]}
    fifth = ({10, 11}, 5)
    print(parse_response(first))
    print(parse_response(second))
    print(parse_response(third))
    print(parse_response(fourth))
    print(parse_response(fifth))

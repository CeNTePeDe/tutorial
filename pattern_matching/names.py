# для pattern matching строка не является последовательностью

def parse_names(value: str | tuple | list | dict) -> str:
    match value:
        case surname, name, second_name: # можно поставитьскобки [] (), это все равно будет сравнение типа
            return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
        case {'surname': surname,
              'name': name,
              'second_name': second_name} if len(value)==3: # но если без ограничения и ключей будет больше,
                                                            # то распаковка произайдет
            return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
        case str() if len(value.split(' ')) == 3:  # проверка типа
                                                   # if выполняется если левая часть, до его была успешна
            surname, name, second_name = value.split(' ')
            return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'

        case _:  # wildcard
            return 'Error'


if __name__ == '__main__':
    assert parse_names(('Иванов', 'Иван', 'Иванович')) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names(['Иванов', 'Иван', 'Иванович']) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names({'surname': 'Иванов',
                        'name': 'Иван',
                        'second_name': 'Иванович'}) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names('Иванов Иван Иванович') == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names(['Иванов', 'Иван']) == 'Error'
    assert parse_names(['Иванов', 'Иван', 'Иван', 'Иван', 'Иван']) == 'Error'
    assert parse_names({'a': 'Иванов', 'b': 'Иван', 'c': 'Иванович'}) == 'Error'
    assert parse_names('Иванов Иван Иванович 122') == 'Error'
    assert parse_names({'surname': 'Иванов',
                        'name': 'Иван',
                        'second_name': 'Иванович',
                        'salary': 100000}) == 'Error'

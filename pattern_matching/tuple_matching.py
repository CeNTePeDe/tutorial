def check(value: tuple):
    match value:
        case (name, _, salary) if name in ('John', 'Ana'):
            return salary
        case ('Helen', age, _):
            return age
        case (_, _, _, _, str(something)):
            return f'Strange! {something}'
        case (*_, something) if len(value) == 6:
            return f'{something}'
        case tuple():
            return f'Unknown connect {value}'
        case _:
            raise ValueError('Expected tuple')


if __name__ == '__main__':
    first = ('Ana', 22, 100_000)
    second = ('Helen', 21, 100_000)
    third = (1, 2, 3, 4, 'Something')
    fourth = (1, 2, 3, 4, 5, 'Something new')
    print(check(first))
    print(check(second))
    print(check(third))
    print(check(fourth))

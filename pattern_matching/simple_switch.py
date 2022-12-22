def calculator(a, b, operation) -> int | str:
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '/':
            return a / b
        case '*':
            return a * b
        case _:  # wildcard
            return f'не знаю такой операции {operation}'


if __name__ == '__main__':
    print(calculator(2, 2, '+'))
    print(calculator(2, 2, '*'))
    print(calculator(2, 2, '-'))
    print(calculator(2, 2, '/'))

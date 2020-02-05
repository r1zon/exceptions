class LenError(Exception):
    pass

def action(a,b,c):
    if c == '+':
        print(int(a) + int(b))
    elif c == '-':
        print(int(a) - int(b))
    elif c == '*':
        print(int(a) * int(b))
    elif c == '/':
        try:
            print (int(a) / int(b))
        except ZeroDivisionError:
            print(f'Делитель равен 0. На ноль делить нельзя.')

def main():
    while True:
        operation = input('Введите выражение для вычисления, для выхода нажмите q: ').split()
        if operation == ['q']:
            break
        else:
            assert operation[0] in ['+', '-', '*', '/'], f'{operation[0]} is not found'
            try:
                if len(operation) != 3:
                    raise LenError()
            except:
                    print('Введено некорректное количество данных')
            else:
                try:
                    int(operation[1])
                    int(operation[2])
                except ValueError:
                    print('Введено НЕ число для выполнения действия.')
                else:
                    action(operation[1], operation[2], operation[0])

main()
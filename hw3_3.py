new_list = list(input('Введите три числа через пробел: ').split(' '))
new_list.sort()


def new_func(*args):
    return args


print(new_func(new_list[-2], new_list[-1]))

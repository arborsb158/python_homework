new_num = list(input('Введите одно положительное и одно отрицательное число через пробел: ').split(' '))
###########################Первый вариант###############


def new_func(x, y):
    return x ** y


print(new_func(int(new_num[0]), int(new_num[1])*(-1)))

##########################Второй вариант#######################


def new_func(x, y):
    i = 1
    n = 1
    while i <= y:
        i += 1
        n = x * n
    return n


print(new_func(int(new_num[0]), int(new_num[1])*(-1)))

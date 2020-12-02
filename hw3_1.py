new_list = list(input('Введите два числа через пробел: ').split())
def new_div(arg_1, arg_2):
    return arg_1 / arg_2

if int(new_list[0]) != 0 and int(new_list[1]) != 0:
    print(new_div(arg_1=int(new_list[0]), arg_2=int(new_list[1])))
else: print('0')

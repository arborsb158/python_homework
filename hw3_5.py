num = 0
try:
    while num != 'q':
        for i in map(int, input('Введите необходимые числа, используя пробел:').split()):
            num += i
        print(num)
        print('Для прерывания программы и выхода, введите "q".')
except ValueError:
    print(num)











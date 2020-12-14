f = open('new_list.txt', 'w')
while True:
    s = input('Введите данные: ')
    f.write(s + '\n')
    if s == '':
        break
f.close()

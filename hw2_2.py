new_list = list(input('Введите необходимое количество переменных: '))
#print(new_list)
#print(len(new_list))
n = 0

if len(new_list) % 2 != 0:
    l = (new_list[-1])
    new_list.pop()
    while n < len(new_list):
        new_list[n],new_list[n+1] = new_list[n+1],new_list[n]
        n = n + 2
    new_list.append(l)
    print(new_list)
else:
    while n < len(new_list):
        new_list[n],new_list[n+1] = new_list[n+1],new_list[n]
        n = n + 2
    print(new_list)




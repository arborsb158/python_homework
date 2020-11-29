my_list = [7, 5, 3, 3, 2]
n = int(input('Введите новое число для включения в список: '))
my_list.append(n)
my_list.sort(reverse=True)
print(my_list)
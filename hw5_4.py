dict_1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('hw5_4_2.txt', 'w', encoding='utf-8') as new:
    with open('hw5_4.txt', 'r', encoding='utf-8') as exist:
        new.write(str([line.replace(line.split()[0], dict_1.get(line.split()[0])) for line in exist]))

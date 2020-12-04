sea_1 = [12, 1, 2]
sea_2 = [3, 4, 5]
sea_3 = [6, 7, 8]
sea_4 = [9, 10, 11]

seasons = {'win': 'Зима', 'spr': 'Весна', 'summer': 'Лето', 'aut': 'Осень'}

n = int(input('Введите порядковый номер месяца в году (1-12): '))

if n in sea_1:
    print(seasons.get('win'))
elif n in sea_2:
    print(seasons.get('spr'))
elif n in sea_3:
    print(seasons.get('summer'))
else:
    print(seasons.get('aut'))

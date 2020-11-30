print('Введите данные по выручке и издержкам предприятия за год.')
proceeds = int(input('Выручка:'))
costs = int(input('Издержки: '))
profit = proceeds - costs
loss = costs - proceeds
profab = profit / proceeds


if proceeds > costs:
    print(f'Предприятие имеет годовую прибыль в размере {profit} рублей.')
    print(f'Рентабельность составила {profab}')
    personal = int(input('Укажите численность сотрудников:'))
    prof_personal = profit / personal
    print(f'Чистая прибыль в пересчете на одного сотрудника составляет {prof_personal} рублей в год')
elif proceeds == costs:
    print('Предприятие на уровне безубыточности')
else:
    print(f'Предприятие имеет годовой убыток в размере {loss} рублей')





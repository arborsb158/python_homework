init_length = int(input('Введите начальное расстояние: '))
goal_length = int(input('Введите целевое расстояние: '))
days = 1

while init_length <= goal_length:
    init_length = init_length*1.1
    days += 1

print(f'На {days}й день спортсмен пробежит не менее {goal_length} километров')
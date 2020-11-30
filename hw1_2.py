time_sec = int(input('Добрый день! Введите время, затраченное на прохождение отрезка в секундах: '))
time_h = (time_sec)//3600
#print(time_h)
time_m = ((time_sec)%3600)//60
#print(time_m)
time_s = (time_sec)%60
#print(time_s)

print(f'Время, потраченное на прохождение участка составило {time_h}:{time_m}:{time_s}.')
from sys import argv

scr_name, total_hours_param, hour_cost_param, bonus_param = argv

print("Имя скрипта: ", scr_name)
print("Количество отработанных часов: ", total_hours_param)
print("Оплата за час: ", hour_cost_param)
print("Премия: ", bonus_param)

print('Общая зарплата равна - ', (int(total_hours_param) * int(hour_cost_param) + int(bonus_param)))



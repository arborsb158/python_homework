salary = open('salary.txt', 'r', encoding='utf-8')
for line in salary:
    words = line.split()
    if int(words[1]) <= 20000:
        print(words[0])
print('имеют зарплату менее 20000 рублей.')

salary.close()

#for line in salary
#print(f' Имена сотрудников с зарплатой меньше 20000: ', words[0])


#target_list = [words[0] for line in salary if int(words[1]) <= 20000]

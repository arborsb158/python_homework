pers_id_list = list(input('Введите через запятую имя, фамилию, год рождения, город проживания, email, телефон:').split(','))

############################Первый вариант###############################

def pers_id(*args):
    return args


print(pers_id(pers_id_list))

#############################второй вариант########################


def pers_id(a, b, c, d, e, f):
    return a, b, c, d, e, f


print(pers_id(a=pers_id_list[0],b=pers_id_list[1],c=pers_id_list[2],d=pers_id_list[3],e=pers_id_list[4],f=pers_id_list[5]))

############################Третий вариант########################

def pers_id(a, b, c, d, e, f):
    print(a, b, c, d, e, f)
pers_id(pers_id_list[0],pers_id_list[1],pers_id_list[2],pers_id_list[3],pers_id_list[4],pers_id_list[5])
from functools import reduce


def new_funk(prev_el, el):
    return prev_el * el


print([el for el in range(99, 1001) if el % 2 == 0])
print(reduce(new_funk, [el for el in range(99, 1001) if el % 2 == 0]))

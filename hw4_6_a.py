from itertools import count
from sys import argv


for el in count(int(argv[1])):
    if el > int(argv[2]):
        break
    else:
        print(el)

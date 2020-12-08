from itertools import cycle
from sys import argv

i = 0
for el in cycle('Hello'):
    if i >= int(argv[1]):
        break
    i += 1
    print(el)

from random import randint
f = open('hw5_5.txt', 'w+')
f.write(' '.join([str(randint(1, 999)) for _ in range (100)]))
f.seek(0)
print(sum(map(int, f.readline().split())))
f.close()

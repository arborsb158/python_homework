num = int(input('Введите многозначное целое число: '))
r = -1
while num > 1:
    d = num % 10
    num //= 10
    if d > r:
        r = d
print(r)
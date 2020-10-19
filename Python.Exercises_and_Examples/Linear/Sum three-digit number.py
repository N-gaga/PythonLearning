import random
v = int(input('1 - Random or 2 - Your number: '))
if v == 1:
    x = random.random() * 900 + 100
    x = int(x)
    print(x)

    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    print(a+b+c)
elif v == 2:
    x = int(input('Input three-digit number: '))

    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    print(a+b+c)
else:
    print('Input 1 or 2')

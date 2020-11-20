from random import randint
n = 10
x = [0] * n

for i in range(n):
    x[i] = randint(0,100)
    print(x[i], end=' ')
print()

minimum = 100
maximum = -1
for i in x:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
print('Maximum: ', maximum)
print('Minium: ', minimum)
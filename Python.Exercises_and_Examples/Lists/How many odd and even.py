from random import random

x = []
for i in range(10):
    n = int(random() * 100)
    x.append(n)

print(x)

even = 0
odd = 0

for i in x:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('Even: ', even)
print('Odd: ', odd)

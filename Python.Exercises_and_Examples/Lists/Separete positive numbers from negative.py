from random import random
x = []
for i in range(10):
    n = int(random() * 20) - 10
    x.append(n)
print(x)
negative = []
positive = []
for i in x:
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)
print(negative)
print(positive)

from random import random, randint

print("Range of integers: ")
xmin = int(input("min = "))
xmax = int(input("max = "))

n = randint(xmin, xmax)
print(n)

print("Range of floats: ")
ymin = float(input("min = "))
ymax = float(input("max = "))

n = random() * (ymax-ymin) + ymin
print("%.3f" % n)

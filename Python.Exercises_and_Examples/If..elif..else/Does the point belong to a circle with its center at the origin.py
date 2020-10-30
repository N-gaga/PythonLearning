import math
x = float(input('x = '))
y = float(input('y = '))
r = float(input('radius = '))

p = math.sqrt(x**2 + y**2)
if p <= r:
    print('Point belongs to the circle')
else:
    print("Point doesn't belong to the circle")
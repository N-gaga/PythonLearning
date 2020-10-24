print('The coordinates:')
x = float(input('x = '))
y = float(input('y = '))

if x > 0 and y > 0:
    print('The 1 quadrant')
elif x < 0 and y > 0:
    print('The 2 quadrant')
elif x < 0 and y < 0:
    print('The 3 quadrant')
elif x > 0 and y < 0:
    print('The 4 quadrant')
elif x == 0 and y == 0:
    print('The point at the origin')
elif x == 0:
    print('The point is on the x-axis')
elif y == 0:
    print('The point is on the y-axis')
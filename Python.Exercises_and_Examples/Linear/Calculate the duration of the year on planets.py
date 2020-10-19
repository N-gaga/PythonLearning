from math import pi

r = float(input('Radius of the orbit (million km): '))
v = float(input('Orbital speed (km/s): '))

r = r * 1000000
t = 2 * pi * r / v
t = t / (60*60*24)

print(round(t))
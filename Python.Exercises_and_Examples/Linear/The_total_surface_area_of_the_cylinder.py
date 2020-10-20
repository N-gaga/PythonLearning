from math import pi

r = float(input("r = "))
h = float(input("h = "))

side = 2*pi*r*h
circles = 2*pi*r**2
area = side + circles
print("The total surface area of the cylinder: %.2f" % area)

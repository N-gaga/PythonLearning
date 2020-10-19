import math

AB = float(input('Length of the first leg: '))
AC = float(input('Length of the first leg: '))

BC = math.sqrt(AB ** 2 + AC ** 2)

S = (AB + AC)/ 2
P = AB + AC + BC

print('S = %2.f' %S)
print('P = %2.f' %P)
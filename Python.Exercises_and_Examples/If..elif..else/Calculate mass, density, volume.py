r = None

x = input('What to calculate? (m, d, v) = ')

if x == 'm':
    d = float(input('Density = '))
    v = float(input('Volume = '))
    r = d * v
elif x == 'd':
    m = float(input('Mass = '))
    v = float(input('Volume = '))
    r = m / v
elif x == 'v':
    m = float(input('Mass = '))
    d = float(input('Density = '))
    r = m / d
print('%.2f' % r)
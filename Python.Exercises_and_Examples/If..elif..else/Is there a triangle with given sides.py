print('Length of the sides:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b>c and b+c>a and a+c>b:
    print('The triangle exists')
else:
    print('The triangle does not exist')


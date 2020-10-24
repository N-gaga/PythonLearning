x = int(input('Year = '))
if x % 4 != 0:
    print('Usual year')
elif x % 100 == 0:
    if x % 400 == 0:
        print('Leap year')
    else:
        print('Usual year')
else:
    print('Leap year')



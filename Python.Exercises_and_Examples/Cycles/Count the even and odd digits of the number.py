x = int(input('Number: '))

even = 0
odd = 0
while x > 0:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x = x // 10
print('Even: %d' % even)
print('Odd: %d' % odd)
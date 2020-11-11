n1 = int(input('An integer: '))
n2 = 0
while n1 > 0:
    n = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + n
print('Inverse number: ', n2)
n1 = int(input('Binary n1: '), 2)
n2 = int(input('Binary n2: '), 2)

b_or = n1 | n2
b_and = n1 & n2
b_xor = n1 ^ n2

b_or = bin(b_or)
b_and = bin(b_and)
b_xor = bin(b_xor)

print('n1: %10s' % n1)
print('n2: %10s' % n2)
print(' ')
print('OR: %10s' % b_or)
print('AND: %10s' % b_and)
print('XOR: %10s' % b_xor)
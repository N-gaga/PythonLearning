first = input('The first:')
last = input('The last:')

while first <= last:
    print(first, end = '')
    first = chr(ord(first) + 1)

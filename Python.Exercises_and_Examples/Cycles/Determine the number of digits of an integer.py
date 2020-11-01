number = int(input('Insert the number: '))
number = abs(number)

count = 1
number //= 10

while number > 0:
    number //= 10
    count += 1
print(count)
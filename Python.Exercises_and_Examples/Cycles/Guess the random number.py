import random

x = 0

number = random.randint(1, 50)

while x < 6:
    y = int(input("Insert the number: "))

    x += 1
    if y < number:
        print('To less!')
    elif y > number:
        print('To much!')
    elif y == number:
        print('You guessed it!')
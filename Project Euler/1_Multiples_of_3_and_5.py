#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
x = 3
y = 5
z = 15
max = 1000
sum = 0
while x < max:
    sum += x
    x += 3
while y < max:
    sum += y
    y += 5
while z < max:
    sum -= z
    z += 15
print(sum)

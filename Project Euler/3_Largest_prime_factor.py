# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Какой самый большой делитель числа 600851475143, являющийся простым числом?

n = 600851475143
x = 2
while 1:
    if n % x == 0:
        n /= x
        if n == 1:
            print(x)
            break
    x += 1




n1 = input("n1 = ")
n2 = input("n2 = ")

a = ord(n1)
b = ord(n2)
print("n1 = %s" % a)
print("n2 = %s" % b)
d = a - b
s = a - ord('0') + b - ord('0')

print("%s-%s=%d" % (n1, n2, d))
print("%s+%s=%d" % (n1, n2, s))

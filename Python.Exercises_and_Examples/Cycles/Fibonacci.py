x = int(input())
f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < x:
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    i += 1
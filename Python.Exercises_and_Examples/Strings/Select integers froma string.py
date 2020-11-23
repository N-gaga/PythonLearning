text = input()
l = len(text)

i = 0
while i < l:
    num = ''
    s = text[i]
    while s.isdigit():
        num += s
        i += 1
        if i < l:
            s = text[i]
        else:
            break
    if num != '':
        print(num)
    i += 1

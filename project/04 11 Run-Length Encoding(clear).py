a = input()
a += ' '
b = ''
c = 1
for i in range(len(a) - 1):
    if a[i+1] == a[i]:
        c += 1
    else:
        b += a[i] + " " + str(c) + " "
        c = 1
print(b)
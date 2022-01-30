n = int(input())
b = ''
for i in range(n):
    a = input()
    if a[0] == '.':
        c = 0
        for k in range(len(a)-1):
            if a[k] == '.' and a[k] == a[k+1]:
                c += 1
            else:
                break
        a = a.replace('.','',int(c/2)+1)
    b += a + "\n"
print(b)
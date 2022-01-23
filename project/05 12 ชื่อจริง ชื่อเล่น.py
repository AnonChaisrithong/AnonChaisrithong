a = ["Robert","Wiliam","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
b = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
N = int(input())
l = []
for i in range(N):
    c = input()
    if c in a:
        k = a.index(c)
        l.append(b[k])
    elif c in b:
        k = b.index(c)
        l.append(a[k])
    else:
        l.append("Not found")
for i in range(len(l)):
    print(l[i])
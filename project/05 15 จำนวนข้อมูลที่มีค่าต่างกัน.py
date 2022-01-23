a = [int(e) for e in input().split()]
a.sort()
b = []

for i in range(0,12):
    if a[i-1] == a[i]:
        a.remove(a[i])

for i in range(len(a)):
    if 0 <= a[i] <= 9:
        b.append(a[i])
print(len(a))
print(b)
print(a[0])
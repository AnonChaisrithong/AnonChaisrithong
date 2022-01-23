a = [float(e) for e in input().split()]
Max = a[0]
for i in a:
    if i > Max:
        Max = i
    else:
        pass
a.remove(Max)
Min = a[0]
for i in range(1,len(a)):
    if a[i] < Min:
        Min = a[i]
a.remove(Min)
av = 0
for i in a:
    av += i
print(av/len(a))
print(Min,Max)
n = int(input())
c = n
a = []
while n != 1:
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    a.append(str(int(n)))
if len(a) > 15:
    new_a = [e for e in a[len(a)-15:len(a)]]
    print("->".join(new_a))
else:
    new_a = a
    print(str(c) + "->" + "->".join(new_a))

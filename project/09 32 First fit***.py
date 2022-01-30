def first_fit(L,e):
    for i in L:
        c = 0
        for k in i:
            c += k
        if c + e <= 100:
            i.append(e)
            break
    return L

def best_fit(L,e):
    check = []
    full = False
    for i in L:
        c = 0
        for k in i:
            c += k
        if c + e == 100:
            i.append(e)
            full = True
            break
        elif c + e < 100:
            check.append(c+e)
    if full == False:
        M = max(check)
        index_L = check.index(M)
        L[index_L].append(e)
    return L

def partition_FF(D):
    c = []
    check = []
    for i in range(len(D)):
        if D[i] not in check:
            c.append([D[i]])
            for k in range(i+1,len(D)):
                if D[k] not in check:
                    if D[i] + D[k] <= 100:
                        a = first_fit(c,D[k])
                        check.append(D[k])
            if type(a) == list and len(a)>0:
                c.append(a)
        else:
            c.append([D[i]])

    return c

print(first_fit([[50],[90]],10))
print(best_fit([[80],[80]],10))
print(partition_FF([50,90,10,80,50,20]))
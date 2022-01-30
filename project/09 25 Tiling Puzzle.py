def row_number(t,e):
    for i in t:
        for k in i:
            if k == e:
                return e
    return "Don't have row number"

def flatten(t):
    a = []
    for i in t:
        for k in i:
            if k == 0:
                i.remove(0)
    for i in t:
        for k in i:
            a.append(k)
    return a

def inversions(x):
    b = list()
    d = 0
    for i in range(len(x)-1):
        for k in range(i,len(x)):
            b.append([x[i],x[k]])
    for i in b:
        if i[0] > i[1]:
            d += 1
    return d

def solvable(t):
    if len(t)%2 != 0:
        if inversions(flatten(t))%2 == 0:
            return True
        else:
            return False
    else:
        for i in t:
            c = 0
            for k in i:
                if k == 0:
                    c += 1
                    break
            if c == 1:
                e = i
                break
        if inversions(flatten(t))%2 == 0:
            if e%2 != 0:
                return True
            else:
                return False
        else:
            if e%2 == 0:
                return True
            else:
                return False

print(row_number([[0,8,7],[6,5,4],[3,2,1]], 0))
print(flatten([[0,8,7],[6,5,4],[3,2,1]]))
print(inversions([8,7,6,5,4,3,2,1]))
print(solvable([[0,8,7],[6,5,4],[3,2,1]]))
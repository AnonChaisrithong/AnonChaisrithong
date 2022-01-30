def reverse(d):
    e = {}
    for i in d:
        e[d[i]] = i
    return e

def keys(d,v):
    e = []
    for i in d:
        if d[i] == v:
            e.append(i)
    return e

print(reverse({3:"A",2:"B"}) == {"A":3,"B":2})
print(keys({3:33, 4:33, 5:55, 2:33}, 33))
print(keys({3:33, 4:33, 5:55, 2:33}, 9999))
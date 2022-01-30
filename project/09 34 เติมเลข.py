def pattern1(nrows, ncols):
    l1 = []
    c = 1
    for i in range(nrows):
        l2 = []
        for k in range(ncols):
            l2.append(c)
            c += 1
        l1.append(l2)
    return l1

def pattern2(nrows,ncols):
    l1 = []
    for i in range(nrows):
        c = i + 1
        l2 = []
        for k in range(ncols):
            l2.append(c)
            c += 3
        l1.append(l2)
    return l1

def pattern3(N):
    l1 = []
    c = 1
    for i in range(N):
        l2 = []
        for k in range(i):
            l2.append(0)
        for k in range(N-i):
            l2.append(c)
            c += 1
        l1.append(l2)
    return l1

def pattern4(N):
    l1 = []
    for i in range(N):
        c = i + 1
        l2 = []
        for k in range(i):
            l2.append(0)
        for k in range(N - i):
            l2.append(c)
            c += k + 2 + i
        l1.append(l2)
    return l1

def pattern5(N):
    l1 = []
    for i in range(N):
        c = i + 1
        l2 = []
        for k in range(i):
            l2.append(0)
        for k in range(N - i):
            l2.append(c)
            c += N - k
        l1.append(l2)
    return l1

def pattern6(N):
    l1 = []
    for i in range(N):
        c = i + 1
        l2 = []
        for k in range(i):
            l2.append(0)
        for k in range(N - i):
            l2.append(c)
            c += N + 2
        l1.append(l2)
    return l1

print(pattern1(3,4))
print(pattern2(3,4))
print(pattern3(4))
print(pattern4(4))
print(pattern5(4))
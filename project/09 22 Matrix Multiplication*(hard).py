def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c,A):
    for i in range(len(A)):
        for k in range(len(A[i])):
            A[i][k] = A[i][k]*c
    return A

def mult(A,B):
    m = []
    if len(A[0]) >= len(B[0]):
        for i in range(len(A)):
            l = []
            j = []
            for k in range(len(A[i])):
                l.append(A[i][k])
            for k in range(len(B[i])):
                c = 0
                for e in range(len(B)):
                    c += l[e]*B[e][k]
                j.append(c)
            m.append(j)
        return m
    else:
        return "ERROR"


A = read_matrix()
B = read_matrix()
print(mult(A,B))
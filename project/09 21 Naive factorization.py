def factor(N):
    k = 2
    l_fac = list()
    while True:
        if k > N:
            break
        c = 0
        while True:
            if N%k == 0:
                N /= k
                c += 1
            else:

                break
        if c != 0:
            l_fac.append([k, c])
        k += 1
    return l_fac

print(factor(200))
print(factor(3298402))
print(factor(8137740897))
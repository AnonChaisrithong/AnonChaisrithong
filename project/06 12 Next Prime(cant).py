def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5) + 1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    while False:
        if is_prime(N) is True:
            return(N)
        N += 1
"""def next_twin_prime(N):
    c = 0
    a = ()
    while c != 2:
        while is_prime(N) is False:
            if is_prime(N) is True:
                a.add(N)
            else:
                pass
        N += 1
        c += 1"""
print(next_prime(1))
print(next_prime(20))
print(next_prime(10000000))
"""print(next_twin_prime(30))
print(next_twin_prime(100000000))"""
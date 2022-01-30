def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def is_coprime(a,b,c):
    e = gcd(a,b)
    f = gcd(b,c)
    g = gcd(a,c)
    i = [-1,1]
    if e not in i and f not in i and g not in i:
        return False
    else:
        return True

def primitive_Pythagorean_triples(max_len):
    triple = []
    for i in range(1,max_len+1):
        for k in range(i+1,max_len+1):
            for e in range(k+1,max_len+1):
                if i**2 + k**2 == e**2 and is_coprime(i,k,e):
                    triple.append([i,k,e])
    return triple

print(is_coprime(2,3,6),is_coprime(2,4,8))
print(primitive_Pythagorean_triples(10))
print(primitive_Pythagorean_triples(20))
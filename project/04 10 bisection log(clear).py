a = float(input())
b = a
L = 0
U = 0
while True:
    U += 1
    b //= 10
    if b == 0:
        break
c = (L+U)/2
while True:
    if 10**c > a:
        U = c
    elif 10**c < a:
        L = c
    if abs(a-10**c) <= 1e-10 * max(a,10**c):
        break
    c = (L+U)/2
print(round(c,6))
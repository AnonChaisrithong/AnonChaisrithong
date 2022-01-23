#x = log10a
a = float(input())
L = 0
U = a
x = (L+U)/2
while True:
    if 10**x > a:
        U = x
    elif 10**x < a:
        L = x
    if abs(a-10**x) <= 1e-10 * max(a,10**x):
        break
    x = (L+U)/2
print(round(x,6))
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = [int(e) for e in input().split()]
    X.append(x)
    Y.append(y)
a = input()
if a == "Zig-Zag":
    m = min(X[::2] + Y[1::2])
    M = max(X[1::2] + Y[::2])
   
else:
    M = max(X[::2] + Y[1::2])
    m = min(X[1::2] + Y[::2])
print(m,M)
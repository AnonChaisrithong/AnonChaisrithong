M = int(input())
N = int(input())
L = []
if len(str(M)) < N:
    for i in range(N - len(str(M))):
        L.append("0")
    for i in str(M):
        L.append(i)
    print("".join(L))
else:
    print(M)
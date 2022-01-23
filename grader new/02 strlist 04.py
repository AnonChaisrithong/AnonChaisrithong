M = input()
N = int(input())
if len(M) >= N:
    print(M)
else:
    print("0"*(N-len(M)) + M)
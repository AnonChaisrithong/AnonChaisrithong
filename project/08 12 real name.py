N = int(input())
d_name = {}
for i in range(N):
    name = input().split()
    d_name[name[0]] = name[1]
rev_d_name = {}
for i in d_name:
    rev_d_name[d_name[i]] = i
M = int(input())
output = []
for i in range(M):
    name_in = input()
    if name_in in d_name:
        output.append(d_name[name_in])
    elif name_in in rev_d_name:
        output.append(rev_d_name[name_in])
    else:
        output.append("Not found")
for i in output:
    print(i)
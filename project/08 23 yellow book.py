N = int(input())
dic_name = {}
for i in range(N):
    first_name,last_name,no = input().split()
    name = [first_name,last_name]
    name = " ".join(name)
    dic_name[name] = no
rev_dic_name = {}
for i in dic_name:
    rev_dic_name[dic_name[i]] = i
M = int(input())
l_want = []
for i in range(M):
    a = input()
    l_want.append(a)
for i in l_want:
    if i in dic_name:
        print(i,"-->",dic_name[i])
    elif i in rev_dic_name:
        print(i,"-->",rev_dic_name[i])
    else:
        print(i, "-->","Not found")
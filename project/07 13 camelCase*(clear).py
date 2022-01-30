a = input()
special_char = "\"(),.-'"
for i in a:
    if i in special_char:
        a = a.replace(i," ",1)
l = a.split()
print(l)
l[0] = l[0].lower()
for i in range(1,len(l)):
    if 'a' <= l[i][0] <= 'z':
        c = l[i][0].upper()
        l[i] = l[i].replace(l[i][0],c,1)
    for k in range(1,len(l[i])):
        if 'A' <= l[i][k] <= 'Z':
            t = l[i][k].lower()
            l[i] = l[i].replace(l[i][k],t,1)
print(''.join(l))
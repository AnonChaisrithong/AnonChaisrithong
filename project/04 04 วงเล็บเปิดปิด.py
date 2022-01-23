a = input()
l = []
for i in a:
    l.append(i)
for i in range(len(l)):
    if l[i] == "(":
        l[i] = "["
    elif l[i] == "[":
        l[i] = "("
    elif l[i] == "]":
        l[i] = ")"
    elif l[i] == ")":
        l[i] = "]"
print("".join(l))
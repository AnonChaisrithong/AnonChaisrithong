u = input().strip("[]")
u = u.split(",")
v = input().strip("[]")
v = v.split(",")
z = []
for i in range(len(u)):
    u[i] = u[i].strip()
    u[i] = float(u[i])
    v[i] = v[i].strip()
    v[i] = float(v[i])
    z.append(float(u[i]) + float(v[i]))
print(u,"+",v,"=",z)

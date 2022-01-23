u = [float(e) for e in input().strip("[ ]").split(",")]
v = [float(e) for e in input().strip("[ ]").split(",")]
sum_unv = [u[0]+v[0] , u[1]+v[1] , u[2]+v[2]]
print(u,"+",v,"=",sum_unv)
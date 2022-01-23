n = int(input())
fulllist = []
for i in range(n):
    x,y = [float(e) for e in input().split()]
    distance = (x**2 + y**2)**0.5
    sublist = [distance,i+1,x,y]
    fulllist.append(sublist)
fulllist.sort()
print("#"+str(fulllist[2][1]) + ":" + " " + "(" + str(fulllist[2][2]) + ", " + str(fulllist[2][3]) + ")")
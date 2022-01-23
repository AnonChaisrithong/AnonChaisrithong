def distance1(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2)**0.5

def distance2(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return distance1(x1,y1,x2,y2)

def distance3(c1,c2):
    C1 = []
    C2 = []
    for i in range(0,2):
        C1.append(c1[i])
        C2.append(c2[i])
    d3 = distance2(C1,C2)
    rt = c1[2] + c2[2]
    if d3 <= rt:
        overlap = True
    else:
        overlap = False
    return d3,overlap

def perimeter(points):
    k = len(points)
    P = 0
    for i in range(k):
        a = (i+1)%k
        P += distance2(points[i],points[a])
    return P

print(distance1(0,0,3,4))
print(distance2([0,0],[3,4]))
A,B = distance3([0,0,1],[5,0,2])
print(A,B)
print(perimeter([[0,0],[0,2],[2,2],[2,0]]))
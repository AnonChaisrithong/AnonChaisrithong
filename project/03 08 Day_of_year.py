a = int(input())
b = int(input())
c = int(input())
d = [31,0,31,30,31,30,31,31,30,31,30,31]
c -= 543
sm = 0
if b == 1:
    pass
else:
    sm += 31
    for i in range(1,b-1):
        sm += d[i]
    if b == 2:
        pass
    else:
        if (c%4 == 0 and c%100 != 0) or (c%400 == 0):
            sm += 29
        else:
            sm += 28

sm += a
print(sm)
import math
a = float(input())
b = float(input())
c = float(input())
numerator = 1/2*((a-b) + (a-c))
denominator = math.sqrt((a-b)**2 + ((a-c)*(b-c)))
seta = math.acos(numerator/denominator)
x = int(360-math.degrees(seta))
print(x)

n = int(input())
a = [0,1]
b = ["zero",'one']
e = a.index(n)
print(b[e])

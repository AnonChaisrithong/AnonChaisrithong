import math
n = int(input())
a = math.sqrt(2*math.pi)*(n**(n+0.5))*(math.e**(1/(12*n+1) - n))
b = math.sqrt(2*math.pi)*(n**(n+0.5))*(math.e**(1/(12*n) - n))
print(a)
print(b)
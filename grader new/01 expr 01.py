import math
n = int(input())
top_range = math.sqrt(2*math.pi) * (n**(n+1/2)) * (math.e**(-n+1/(12*n+1)))
low_range = math.sqrt(2*math.pi) * (n**(n+1/2)) * (math.e**(-n+1/(12*n)))
print(top_range)
print(low_range)
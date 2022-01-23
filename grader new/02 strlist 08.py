import math
a = input().split(",")
part = int("9"*len(a[2]) + "0"*len(a[1]))
scrab = int(a[1]+a[2]) - int("0"+a[1])
odd = int(a[0]) * part
gcd = math.gcd(odd+scrab,part)
print((odd+scrab)//gcd,"/",part//gcd) #// เพราะไม่ต้องการจุดทศนิยม
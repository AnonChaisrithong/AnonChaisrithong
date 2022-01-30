a,b,c = input().split(",")
e = ""
e += "9"*len(c)
e += "0"*len(b)
d = int(a)*int(e) + (int(b+c) - int("0"+b ))  # answer = d/int(e) and บวก "0"ไป เพื่อกันเป็นstring ปล่าง
import math
gcd = math.gcd(d,int(e))
d = d/gcd
e = int(e)/gcd
print(d,"/",e)
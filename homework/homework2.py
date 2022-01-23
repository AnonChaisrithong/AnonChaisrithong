# ให้เขียนโปรแกรมในเซลล์นี้เท่านั้น ห้ามลบ/แก้ไข ข้อความในบรรทัดแรกนี้ 
import math 

def term_k(x,k):
    a = (-1)**k * (x**(2*k + 1))
    b = math.factorial(2*k + 1)
    return a/b



def approximated_sin(x):
    k = 0
    approx_sin = 0
    while True:
        approx_sin += term_k(x,k)
        if find_eff(math.sin(x),approx_sin) < 1e-6:
            print(k)
            break
        else:
            k+=1
    return approx_sin



def find_eff(a,b):
    return math.sqrt((a-b)**2)



print(find_eff(math.sin(10),approximated_sin(10))) # ค่าที่ได้จะต้องน้อยกว่า 10**(-6)
print(10e-6 == 10**(-6))
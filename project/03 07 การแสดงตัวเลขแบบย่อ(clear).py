n = int(input())
if n < 1000:
    print(n)
elif 1000 <= n < 10000:
    if n%100 >= 50:
        print(str((n//100)/10 + 0.1) + 'K')
    else:
        print(str((n//100)/10) + 'K' )
elif 10000 <= n < 1e6:
    if n%1000 >= 500:
        print(str(n//1000 + 1) + 'K')
    else:
        print(str(n//1000) + 'K')
elif 1e6 <= n < 10e6:
    if n%100000 >= 50000:
        print(str(round((n//100000)/10 + 0.1 , 1)) + 'M')
    else:
        print(str(n//100000/10) + 'M')
elif 10e6 <= n < 1000e6:
    if n%1000000 >= 500000:
        print(str(n//1000000 + 1) + 'M')
    else:
        print(str(n//1000000) + 'M')
elif 1000e6 <= n < 10000e6:
    if n%100000000 >= 50000000:
        print(str(round(n//100000000/10 + 0.1 ,1)) + 'B')
    else:
        print(str(n//100000000/10) + 'B')
else:
    if n%1000000000 >= 500000000:
        print(str(n//1000000000 + 1) + 'B')
    else:
        print(str(n//1000000000) + 'B')
"""
เฉลย
n = int(input())
if(n<1000):
    print(n)
elif(n<10000):
    print(str(round(n / 1000, 1))+"K")
elif(n<1000000):
    print(str(int(round(n,-3)/1000))+"K")
elif(n<10000000):
    print(str(round(n / 1000000, 1)) + "M")
elif(n<1000000000):
    print(str(int(round(n,-6)/1000000))+"M")
elif(n<10000000000):
    print(str(round(n / 1000000000, 1)) + "B")
else:
    print(str(int(round(n, -9) / 1000000000)) + "B")
โคตรง่าย ทำไมกูต้องคิดเยอะ
"""

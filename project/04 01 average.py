n = input()
s = 0
k = 0
while n != "q":
    s += float(n)
    k += 1
    n = input()

if s == 0:
    print("No Data")
else:
    print(round(s/k,2))

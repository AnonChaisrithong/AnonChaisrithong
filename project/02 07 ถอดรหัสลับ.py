a = input()
b = ""
for i in a[3::7]:
    b += i
c = ""
for i in a[7::5]:
    c += i
s = int(b)+int(c)+10000
k = str(s%10000)[0:3]
e = 0
for i in range(len(k)):
    e += int(k[i])
f = int(str(e)[len(str(e))-1]) + 1
Alpha = ["0","A","B","C","D","E","F","G","H","I","J"]
print(k + Alpha[f])
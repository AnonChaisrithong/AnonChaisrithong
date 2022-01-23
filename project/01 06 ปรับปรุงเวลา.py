h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
dh = 0
if s2 < s1:
    m2 -= 1
    s2 += 60
ds = s2 - s1
if m2 < m1:
    h2 -= 1
    m2 += 60
dm = m2 - m1
if h2 < h1:
    dh = 24 + h2 - h1
else:
    dh = h2 - h1
print(str(dh) + ":" + str(dm) + ":" + str(ds))
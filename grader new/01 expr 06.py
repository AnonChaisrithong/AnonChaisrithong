h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

if s2>=s1:
    s = s2-s1
else:
    m2 -= 1
    s = s2+60-s1

if m2>=m1:
    m = m2-m1
else:
    h2 -= 1
    m = m2+60-m1

if h2>=h1:
    h = h2-h1
else:
    h = 24-(h1-h2)

print(str(h) + ":" + str(m) + ":" + str(s))
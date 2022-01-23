Card = [e for e in input().split()]
b = []
c = []
for i in range(0,len(Card)/2):
    b.append(Card[i])
for i in range(len(Card)/2,len(Card)):
    c.append(Card[i])
CNS = input()

for i in CNS:
    L = []
    if i == "C":
        for k in range(len(c)):
            L.append(c[k])
        for k in range(len(b)):
            L.append(b[k])
    elif i == "S":
        for k in range(len(b)):
            L.append(b[k])
            L.append(c[k])
    else:
        pass
    if i == "C" or i == "S":
        Card = L
        b = []
        c = []
        for k in range(0, len(Card)/2):
            b.append(Card[k])
        for k in range(len(Card)/2, len(Card)):
            c.append(Card[k])
    else:
        pass
print(" ".join(Card))
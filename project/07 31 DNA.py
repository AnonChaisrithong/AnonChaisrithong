DNA = input()
DNA = DNA.upper()
operater = input()
b = "ATGC"
if operater == "R":
    a = []
    Invalid0 = False
    for i in DNA:
        if i not in b:
            Invalid0 = True  
    for i in DNA:
        if i == "A":
            i = "T"
            a.append(i)
        elif i == "C":
            i = "G"
            a.append(i)
        elif i == "T":
            i = "A"
            a.append(i)
        elif i == "G":
            i = "C"
            a.append(i)
    if Invalid0:
        print("Invalid DNA")
    else:
        a = "".join(a)
        a = a[::-1]
        print(a)

elif operater == "F":
    A = 0
    C = 0
    G = 0
    T = 0
    Invalid = False
    for i in DNA:
        if i not in b:
            Invalid = True
    for i in DNA:
        if i in b:
            if i == "A":
                A += 1
            elif i == "C":
                C += 1
            elif i == "G":
                G += 1
            elif i == "T":
                T += 1
    if Invalid:
        print("Invalid DNA")
    else:
        print("A" + "=" + str(A) + ",", "T" + "=" + str(T) + ",", "G" + "=" + str(G) + ",", "C" + "=" + str(C))
elif operater == "D":
    interest = input()
    c = 0
    for i in range(1,len(DNA)):
        if DNA[i-1] == interest[0] and DNA[i] == interest[1]:
            c += 1
    print(c)
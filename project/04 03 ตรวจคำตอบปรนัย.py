a = input()
b = input()
c = 0
if len(a) == len(b):
    for i in range(len(a)):
        if b[i] == a[i]:
            c += 1
    print(c)
else:
    print("Incomplete answer")
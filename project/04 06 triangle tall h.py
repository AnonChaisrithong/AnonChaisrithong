h = int(input())
print(" "*(h-1) + "*")
for i in range(2,h):
    c = (" "*(h-i) + "*" + " "*(2*i-3) + "*")
    print(c)
print("*"*(2*h-1))

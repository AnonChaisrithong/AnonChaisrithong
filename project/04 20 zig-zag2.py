a = input()
x,y = a.split
X = x + ' '
Y = y + ' '
while True:
    a = input()
    if a == "Zig-Zag" or a == "Zag-Zig":
        break    
    else:
        x,y = a.split()
        X += x + ' '
        Y += y + ' '

if a == "Zig-Zag":
    M = 

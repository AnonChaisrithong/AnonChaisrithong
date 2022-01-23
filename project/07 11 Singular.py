a = input()
b = ["s","x"]
d = "aeiou"
if a[len(a)-1] in b or a[-1:len(a)-2] is "ch":
    a += "es"
elif a[len(a)-1] is "y":
    if a[len(a)-2] in d:
        a += "s"
    else:
        a = a.replace("y","i")
        a += "es"
else:
    a += 's'
print(a)
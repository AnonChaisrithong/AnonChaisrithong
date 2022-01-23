a = input()
alpha = ["0","1","2","3","4","5","6","7","8","9"]
for i in a:
    if i in alpha:
        alpha.remove(i)
print(",".join(alpha))
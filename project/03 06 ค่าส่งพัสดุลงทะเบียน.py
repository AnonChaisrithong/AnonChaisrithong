a = int(input())
b = 0
Reject = False
if a <= 100:
    b += 18
elif 100 < a <= 250:
    b += 22
elif 250 < a <= 500:
    b += 28
elif 500 < a <= 1000:
    b += 38
elif 1000 < a <= 2000:
    b += 58
else:
    Reject = True
if Reject:
    print("Reject")
else:
    print(b)
b = input()
Not_mobile_number = True
a = ["06","08","09"]
if len(b) == 10:
    if b[0:2] in a:
        Not_mobile_number = False
if Not_mobile_number:
    print("Not a mobile number")
else:
    print("Mobile number")

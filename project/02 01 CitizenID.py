ID = input()
sum_ID = 0
for i in range(len(ID)):
    sum_ID += int(ID[i])*(13-i)
n12 = (11 - (sum_ID%11))%10
print(ID[0] + " " + ID[1:5:] + " " + ID[5:10:] + " "  + ID[10::] + " " + str(n12))
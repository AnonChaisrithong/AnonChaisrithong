"""p = input().strip("{ }").split(",")
dic_p = {}
for i in p:
    i = i.split(":")
    key,value = i
    dic_p[int(key)] = int(value)
p = dic_p
"""
def total(pocket):
    total = 0
    for i in pocket:
        total += i*pocket[i]
    return total

def take(pocket,money):
    for i in money:
        if i in pocket:
            pocket[i] += money[i]
        else:
            pocket[i] = money[i]
    return pocket

def pay(pocket,amt):
    initial_pocket = {}
    for i in pocket:
        initial_pocket[i] = pocket[i]
    l_pocket = []
    for i in pocket:
        l_pocket.append([pocket[i],i])
    l_pocket.sort()
    pay_count = 0
    for i in pocket:
        if amt >= i:
            while pocket[i]*i <= amt and pocket[i]>0:
                pay_count += i
                pocket[i] -= 1
                amt -= i
        pay_count = 0
    dif_pocket = {}
    for i in pocket:
        dif_pocket[i] = initial_pocket[i] - pocket[i]
    if amt > 0 :
        return str({}) + "\n" + str(initial_pocket)
    else:
        return str(dif_pocket) + '\n' + str(pocket)

print(total({100:2,50:2,5:2,1:2}))
print(" ")
print(take({100:5},{100:2,1:3}))
print(" ")
print(take({100:5},{100:0,1:0}))
print(" ")
print(pay({10:5,1:7},12))
print(" ")
print(pay({10:5,1:7},18))
print(" ")
print(pay({10:5,1:7},100))
print(" ")
print(pay({10:5,1:7},57))
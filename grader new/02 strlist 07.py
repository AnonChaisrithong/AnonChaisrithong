code = input()
number = [1,2,3,4,5,6,7,8,9,10]
chars = ["A","B","C","D","E","F","G","H","I","J"]
n1 = int(code[3::7])
n2 = int(code[7::5])
nt = n1 + n2 + 10000
nt = str(nt)
unit = nt[-2:-5:-1]
unit = unit[::-1]
key = int(unit[0]) + int(unit[1]) + int(unit[2])
tochar = number.index(int(str(key)[-1])+1)
print(str(unit) + chars[tochar])
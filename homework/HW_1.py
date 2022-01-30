#char is 0123456789!@#gE=-Io
import random
a = "0123456789#@!EqIo-=1456@!-=oqIE12498##@!1-=55EIqE430@"
list_ = []
g = ''
print(len(a))
for i in a:
    list_.append(i)
c = 0
for i in range(37):
    random.shuffle(list_)
    b = "".join(list_)
    for i in b:
        if i not in g:
            g += i
    g = sorted(g)
    print(''.join(g))
    c += 1
print(c)
print(len(a))
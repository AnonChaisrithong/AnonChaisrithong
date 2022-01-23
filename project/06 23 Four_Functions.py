def make_int_list(x):
    return x.split()

def is_odd(e):
    e = int(e)
    if e%2 != 0:
        return True
    else:
        return False
    
def odd_list(alist):
    alis = []
    for i in alist:
        if is_odd(i) is True:
            alis.append(i)
    return alis

def sum_square(alist):
    s = 0
    for i in alist:
        i = i**2
        s += i
    return s

print(make_int_list('1 2 3 4 5'))
print(is_odd(3333))
print(odd_list([1,2,3,4,5,6,7]))
print(sum_square([1,1,2,3]))
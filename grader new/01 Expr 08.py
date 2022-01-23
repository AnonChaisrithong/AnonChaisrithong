def sqrt_n_times(x,n):
    x **= 1/(2**n)
    return x

def cube_root(y):
    y = sqrt_n_times(y,2)
    for i in [2,4,8,16,32]:
        y *= sqrt_n_times(y,i)
    return y

def main():
    q = float(input())
    print(cube_root(q))

print(sqrt_n_times(10**8,3))
print(round(cube_root(27), 4))
print(cube_root(5)**3, (5**(1/3))**3)
main()
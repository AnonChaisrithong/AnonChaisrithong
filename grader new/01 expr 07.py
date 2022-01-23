def mosteller(w,h):
    return ((w*h)**0.5) / 60

def du_bois(w,h):
    return 0.007184 * (w**0.425) * (h**0.725)

def fujimoto(w,h):
    return 0.008883 * (w**0.444) * (h**0.663)

def main():
    weight = float(input())
    height = float(input())
    m = mosteller(weight,height)
    d = du_bois(weight,height)
    f = fujimoto(weight,height)
    print("Mosteller =", round(m,5))
    print("Du Bois =", round(d,5))
    print("Fujimoto =",round(f,5))

print(mosteller(56,173))
print(du_bois(56,173))
print(fujimoto(56,173))
main()
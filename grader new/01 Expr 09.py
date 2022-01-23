def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:] + ':' + ('0'+str(s))[-2:]

def to_sec(h,m,s):
    return h*3600 + m*60 + s

def to_hms(s):
    s2h = s//3600
    s2m = (s-(s2h*3600))//60
    s2s = s-(s2m*60)-(s2h*3600)
    return s2h,s2m,s2s

def diff(h1,m1,s1,h2,m2,s2):
    if s2<s1:
        m2 -= 1
        s = s2+60-s1
    else:
        s = s2-s1
    if m2<m1:
        h2 -= 1
        m = m2+60-m1
    else:
        m = m2-m1
    h = h2-h1
    return h,m,s

def main():
    hms_start = input()
    hms_end = input()
    h1,m1,s1 = str2hms(hms_start)
    h2,m2,s2 = str2hms(hms_end)
    h,m,s = diff(h1,m1,s1,h2,m2,s2)
    print(hms2str(h,m,s))

print(to_sec(10,3,29))
h,m,s = to_hms(36209)
print(h,m,s)
h,m,s = to_hms(36209)
print(hms2str(h,m,s))
dh,dm,ds = diff(10,57,57,12,0,0)
print(dh,dm,ds)
main()
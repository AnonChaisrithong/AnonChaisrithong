mname = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def read_date():
    d,m,y = [e for e in input().split()]
    return [int(d),mname.index(m),int(y)]

def zodiac(d1,m1):
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 : z1 = "Aries"
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 : z1 = "Taurus"
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 : z1 = "Gemini"
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 : z1 = "Cancer"
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 : z1 = "Leo"
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 : z1 = "Virgo"
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 : z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 : z1 = "Capricorn"
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 : z1 = "Aquarius"
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 : z1 = "Pisces"
    return z1

def days_in_feb(y):
    if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
        return 29
    else:
        return 28

def days_in_month(m,y):
    a = [3,5,8,10]
    dim = 0
    for i in range(m):
        if i in a:
            dim = 30
        elif i == 1:
            dim = days_in_feb(y)
        else:
            dim = 31
    return dim

def days_in_month_total(m,y):
    k = 0
    for i in range(m):
        k += days_in_month(i,y)
    return k

def days_in_year(y):
    if days_in_feb(y) == 29:
        return 366
    else:
        return 365

def days_in_between(d1,m1,y1,d2,m2,y2):
    dayall = 0
    day1 = days_in_year(y1) - (days_in_month_total(m1,y1) + d1)
    day2 = days_in_month_total(m2,y2) + d2
    for i in range(y1+1,y2):
        dayall += days_in_year(i)
    dayall = dayall + day1 + day2
    return dayall

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

print(read_date())
print(zodiac(2,9))
print(days_in_feb(2016))
print(days_in_month(2,2017))
print(days_in_between(1,1,2016,1,1,2017))
main()
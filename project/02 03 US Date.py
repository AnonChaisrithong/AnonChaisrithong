day,month,year = [int(e) for e in input().split("/")]
month_US = ["Jan","Feb","May","March","June","July","April","Aug","Sep","Oct","Nov","Dec"]
print(month_US[month-1] , str(day) + " , " + str(year))
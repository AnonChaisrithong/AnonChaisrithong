date = input().split("/")
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(month[int(date[1])-1] + " " + str(date[0]) + "," + " " + str(date[2]))
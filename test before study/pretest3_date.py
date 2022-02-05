d,m,y = input().split('/')
months_of_year = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
trans_date = '*' + ' DATE: ' + d + '.' + months_of_year[int(m)-1] + '.' + y +' ' +  '*'
print('*'*len(trans_date))
print(trans_date)
print('*'*len(trans_date))
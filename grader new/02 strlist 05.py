income = [int(e) for e in input().strip().split()]
total_income = 0
for i in income:
    total_income += i
print(total_income)
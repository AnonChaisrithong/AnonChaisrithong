N = int(input())
dic_name = {}
for i in range(N):
    name = input().split()
    dic_name[name[0]] = int(name[1])
M = int(input())
Total_sales = 0
dic_sell = {}
for i in range(M):
    sell = input().split()
    if sell[0] in dic_name:
        Total_sales += dic_name[sell[0]] * int(sell[1])
        if sell[0] not in dic_sell:
            dic_sell[sell[0]] = int(sell[1])*dic_name[sell[0]]
        else:
            dic_sell[sell[0]] += int(sell[1])*dic_name[sell[0]]
m = 0
max_list = []
for i in dic_sell:
    sub_list = [dic_sell[i],i]
    max_list.append(sub_list)
    if dic_sell[i] > m:
        m = dic_sell[i]
Top_list = []
for i in range(len(max_list)):
    if max_list[i][0] == m:
        Top_list.append(max_list[i][1])
Top_list.sort()
Top_list = ", ".join(Top_list)
if Total_sales == 0:
    print("No ice cream sales")
else:
    print("Total ice cream sales:", Total_sales)
    print("Top sales:" , Top_list)
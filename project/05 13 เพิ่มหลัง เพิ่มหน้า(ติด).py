first_n = int(input())
list = []
for i in range(first_n):  
    first_set_num = int(input())
    list.append(first_set_num)
second_set_num = [int(e) for e in input().split()]
third_set_num = int(input())
list2 = []
while third_set_num != -1: 
    third_set_num = int(input())
    list2.append(third_set_num)
final_list = []
final_list.append(list2[::2])
final_list.append(second_set_num[::2])
final_list.append(list[::2])
print(final_list)
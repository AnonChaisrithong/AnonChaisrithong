first_char = input().lower()
second_char = input().lower()
for i in first_char:
    if i == " ":
        first_char = first_char.replace(i,"")
        break
for i in second_char:
    if i == " ":
        second_char = second_char.replace(i,'')
        break
first_sort = sorted((first_char))
second_sort = sorted((second_char))
if first_sort == second_sort:
    print("YES")
else:
    print("NO")
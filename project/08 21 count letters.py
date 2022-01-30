letters = input().strip().lower()
d_letters = {}
for i in letters:
    if i not in d_letters:
        d_letters[i] = 1
    else:
        d_letters[i] += 1
l_count = []
for i in d_letters:
    sub_list = [-d_letters[i],i]
    l_count.append(sub_list)
l_count.sort()
for i in range(len(l_count)):
    print(l_count[i][1], "->",-l_count[i][0])
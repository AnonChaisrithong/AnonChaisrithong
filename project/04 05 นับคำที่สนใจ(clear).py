interested_word = input()
words = input()
special_char = "\"(),.'"
for i in words:
    if i in special_char:
        words = words.replace(i,"",1)
        words += " "
words = words.split()
c = 0
for i in words:
    if interested_word == i:
        c += 1
print(c)

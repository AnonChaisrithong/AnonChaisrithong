dic_keys2text = {"0":" ","2":"a","22":"b","222":"c","3":"d","33":"e","333":"f","4":"g","44":"h","444":"i","5":"j","55":"k","555":"l","6":'m','66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s','8':'t','88':'u','888':'v','9':'w','99':'x','999':'y','9999':'z'}
dic_text2keys = {}
for i in dic_keys2text:
    dic_text2keys[dic_keys2text[i]] = i
def text2keys(text):
    text = text.lower()
    keys = ''
    for i in text:
        if 'a' <= i <= 'z':
            pass
        elif i.isspace() == True:
            pass
        else:
            text = text.replace(i,"")
    for i in text:
        keys += dic_text2keys[i] + " "
    return keys
def keys2text(keys):
    l_keys = keys.split()
    text = ''
    for i in l_keys:
        text += dic_keys2text[i]
    return text
print(text2keys("Ok, Python"))
print(text2keys("I am busy."))
print(keys2text("444 0 2 6 0 22 88 7777 999"))

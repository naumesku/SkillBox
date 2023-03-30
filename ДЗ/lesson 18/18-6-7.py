def didg(text):
    texts = ''
    for i in text:
        if i.isdigit():
            texts += i
    return texts
text = input ('Введите строку: ')
print(didg(text))

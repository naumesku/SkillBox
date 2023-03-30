text = 'Здесь что-то написано'
text_new = dict()
for i in text.lower():
    if i in text_new:
        text_new [i] += 1
    else:
        text_new [i] = 1
for i in sorted(text_new.keys()):
    print(i," : ",text_new [i])
print('максимальная частота: ', max(text_new.values()))

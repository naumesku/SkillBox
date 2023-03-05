text = input ('Введите строку: ')
new_text=[]
count = 0
for i in list(text):
    if i == ':':
        new_text.append(';')
        count += 1
    else:
        new_text.append(i)
print ('Исправленная строка: ',  end='')
for i in new_text:
    print( i, end='')
print ('\nКоличество замен ', count)







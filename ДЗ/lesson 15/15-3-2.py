text = input ('Введите строку: ')
num_symbol = int (input('Номер символа: '))
texts = list (text)
new_text = []
for i in texts:
    new_text.append(i)
print('Символ слева: ', new_text[num_symbol - 2])
print('Символ справа: ', new_text[num_symbol])
if new_text[num_symbol-2]==new_text[num_symbol-1]==new_text[num_symbol]:
    print('Есть два таких же символов ')
elif new_text[num_symbol-2]==new_text[num_symbol-1] or new_text[num_symbol-1]==new_text[num_symbol]:
    print('Есть ровно один такой же символ ')
else:
    print('Таких же символов нет ')




def change (symb,shift, lists):
    for i in lists:
        if i == symb:
            return lists[(lists.index(i)+shift)%33]
    else:
        return symb
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input ('Введите сообщение: ')
shift = int(input ('Введите сообщение: '))
print('Зашифрованное слово: ', end='')
text_change = [change(i,shift,alphabet) for i in text]
for i in text_change:
    print (i, end ='')

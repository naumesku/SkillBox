def change (symb,shift, lists):
    for i in lists:
        if i == symb:
            return lists[(lists.index(i)+shift)%33]
    else:
        return symb
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input ('Введите сообщение: ').lower()
shift = int(input ('Введите сдвиг: '))
print('Зашифрованное слово: ', end='')
text_change = [change(i,shift,alphabet) for i in text]
print (''.join(text_change))
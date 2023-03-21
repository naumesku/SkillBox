def gbs (a):
    gb = ['а', 'у', 'о', 'ы', 'и', 'й', 'э', 'я', 'ю', 'ё', 'е']
    for i in gb:
        if a == i:
            return True
    else:
        return False
text = input('Введите текст: ')
text = [x for x in text if gbs(x)]
print ('Список гласных букв: ',text)
print ('Длина списка:  ',len(text))

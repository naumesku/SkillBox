cont_book = dict()
while True:
    print ('\nТекущие контакты на телефоне: ')
    for i in cont_book:
        print(i, cont_book[i])
    name = input ('\nВведите имя: ')
    if name == 'end':
        print ('Конец списка')
        break
    elif not name in cont_book:
        cont_book[name]=input('Введите номер телефона: ')
    else:
        print('Ошибка: такое имя уже существует.')

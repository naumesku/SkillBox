phone_book = dict()
while True:
    name = input ('Введите имя контакта: ')
    last_name = input ('Введите Фамилию контакта: ')
    if (name, last_name) not in phone_book:
        phone = int(input('Введите номер телефона: '))
        phone_book[name, last_name] = phone
    else:
        print('Этот контакт уже есть в сиписке. попробуйте еще раз: ')
    print ('Телефонная кника: ',phone_book)
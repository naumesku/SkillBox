phone_book = dict()
def add ():
    name = input ('Введите имя контакта: ').title()
    last_name = input ('Введите Фамилию контакта: ').title()
    if (name, last_name) in phone_book:
        print ('Этот контакт уже зарегестрирован. ')
    else:
        phone = int(input('Введите номер телефона: '))
        phone_book[name,last_name] = phone
def fnd():
    name = input ('Введите имя контакта: ').title()
    last_name = input ('Введите Фамилию контакта: ').title()
    if (name, last_name) in phone_book:
        print ('Телефон контакта: ', phone_book[name, last_name])
    else:
        print ('Такого контакта нет с книге. ')

while True:
    ecs = input ('\tВыберите действие: найти или добавить: ').lower()
    if ecs == 'найти':
        fnd()
    elif ecs == 'добавить':
        add()
    else:
        print ('Такого действия нет, попробуйте еще раз')
    print ('Телефонная кника: ',phone_book)
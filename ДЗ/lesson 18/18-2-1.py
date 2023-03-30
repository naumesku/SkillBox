name = input ('Имя: ')
number = int (input ('Номер заказа '))
pattern = 'Здравствуйте, {us_name} ! Ваш номер заказа: {us_number}. Приятного дня!'.format(us_name = name, us_number = number)
print (pattern)
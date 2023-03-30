name = input ('Введите имя: ')
debt = int(input ('Введите долг: '))
reminder = '{us_name}! {us_name}, привет! Как дела, {us_name}?' \
           ' Где мои {us_debt} рублей? {us_name}!'.format(
    us_name=name,
    us_debt = debt)
print (reminder)

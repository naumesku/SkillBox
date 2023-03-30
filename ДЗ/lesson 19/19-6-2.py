def cntr (city,countrys):
    for i in countrys:
        if city in countrys[i]:
            print('Город ', city, ' расположен в стране ', i, '.')
            break
    else:
        print('По городу ', city, ' данных нет. ')

n = int (input ('Кол-во стран: '))
countrys= dict()
for i in range (n):
    print (i+1,' страна: ', end ='')
    country = input().split(' ')
    countrys[country[0]] = ','.join(country[1:])
    print(countrys)
for n in range(3):
    print (n+1,' город: ', end ='')
    city = input()
    cntr(city, countrys)






# Пример:
# Кол-во стран: 2
# 1 страна: Россия Москва Петербург Новгород
# 2 страна: Германия Берлин Лейпциг Мюнхен
#
# 1 город: Москва
# Город Москва расположен в стране Россия.
#
# 2 город: Мюнхен
# Город Мюнхен расположен в стране Германия.
#
# 3 город: Рим
# По городу Рим данных нет.

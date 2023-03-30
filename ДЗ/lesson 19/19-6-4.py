def sum_m(good,store):
    sum=0
    for i in store[good]:
        sum += i['quantity']
    return sum

def sum_p(good,store):
    sum=0
    for i in store[good]:
        sum += (i['price']*i['quantity'])
    return sum

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
print('Результат работы программы.')
for i in goods:
    print (i,'-',sum_m(goods[i],store),'шт, стоимость ',sum_p(goods[i],store) , 'руб')
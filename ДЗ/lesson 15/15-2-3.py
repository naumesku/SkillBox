N = int(input('Введите количество собак '))
list = []
new_list = []
for i in range(N):
    print('Сколько очков у ', i+1, '-ой собаки ', end='')
    coin = int(input())
    list.append(coin)
print ('Не верный список', list)

#Находим макс и мин
max = list[1]
min = list[1]
for n in list:
    if max < n:
        max = n
    if min > n:
        min = n
print ('max = ',max, 'min = ', min)

# Меняем макс и мин местами
for i_coin in list:
    if i_coin == min:
        new_list.append(max)
    elif i_coin == max:
        new_list.append(min)
    else:
        new_list.append(i_coin)
print ('Верный список', new_list)
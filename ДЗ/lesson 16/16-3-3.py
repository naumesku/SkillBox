general_list = []
pack = []
coin = 0
n = int(input('Количество пакетов '))
for p in range(n):
    print('\nПакет номер: ', p + 1)

    for bit in range(4):
        print(bit + 1, 'Бит номер: ', end='')
        b = int(input())
        pack.append(b)
    if pack.count(-1) <= 1:
        general_list.extend(pack)
    else:
        print('Много ошибок в пакете. ')
        coin += 1
    pack = []
print('Полученное сообщение: ', general_list)
print('Кол-во ошибок в сообщении: ', general_list.count(-1))
print('Кол-во потерянных пакетов: ', coin)

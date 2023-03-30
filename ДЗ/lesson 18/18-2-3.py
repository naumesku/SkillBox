num_list = []
for i in range (4):
    while True:
        print('Введите',i +1,'число: ', end ='')
        num = int(input())
        if 0<= num <= 255:
            break
        else:
            print ('Число должно быть в пределах от 0 до 255')
    num_list.append (num)
ip_address = '{0}.{1}.{2}.{3}'.format(num_list[0],num_list[1],num_list[2],num_list[3])
print ('IP- адрес: ', ip_address)

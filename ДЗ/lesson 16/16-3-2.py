messeng_1 = list (input ('Первое сообщение: '))
messeng_2 = list (input ('Второе сообщение: '))

if (messeng_1.count('!') + messeng_1.count('?'))>(messeng_2.count('!') + messeng_2.count('?')):
    messeng_1.extend(messeng_2)
    print('Третье сообщение: ', end='')
    for i in range (len(messeng_1)):
        print(messeng_1[i], end='')
elif (messeng_1.count('!') + messeng_1.count('?')) == (messeng_2.count('!') + messeng_2.count('?')):
         print ('Ой')
else:
     messeng_2.extend(messeng_1)
     print('Третье сообщение: ', end='')
     for i in range(len(messeng_2)):
         print(messeng_2[i], end='')

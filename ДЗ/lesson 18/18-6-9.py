def lim (ip):
  if len(ip.split('.')) != 4:
    print('Адрес - это четыре числа, разделенные точками')
  else:
    for i in ip.split('.'):
      if not i.isdigit():
        print(i,' - не целое число. ')
        break
      elif int(i) >255:
        print (i, 'превышает 255. ')
        break
      elif int(i)<0:
        print (i, 'не может быть ниже 0. ')
        break
    else:
      print ('IP-адрес корректен. ')
ip=input('Введите IP: ')
lim (ip)
data = dict()
n = int (input('Введите кол-во заказов: '))
for i in range (n):
  print (i+1,'заказ: ', end='')
  ord = input().split(' ')
  if ord[0] in data:
    if ord[1] in data[ord[0]]:
      data[ord[0]][ord[1]] += int(ord[2])
    else:
      data[ord[0]][ord[1]] = int(ord[2])
  else:
    data[ord[0]] = {ord[1] : int(ord[2])}
for i in data:
  print (i,':')
  for n in data[i]:
    print('\t',n, ':' ,data[i][n])







#Введите кол-во заказов: 6
# 1 заказ: Иванов Пепперони 1
# 2 заказ: Петров Де-Люкс 2
#3 заказ: Иванов Мясная 3
#4 заказ: Иванов Мексиканская 2
#5 заказ: Иванов Пепперони 2
#6 заказ: Петров Интересная 5


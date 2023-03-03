x = input ('Выберите операцию: ')
while x!= '+' and x!='-' and x!='*' and x!='/':
  x = input ('Ошибка: такой операции не существует. Попробуйте ещё раз.')
op = int (input ('Сколько операндов? '))
count = 1

if x == '+':
  summ = 0
  sum = ''
  while op !=0:
    print ('Введите операнд №', count, end = ':\t')
    a = int(input())
    count += 1
    op -= 1
    summ += a
    sum += str (a)
    if op!=0:
      sum += '+'
  print (sum, '=' , summ)

elif x == '-':
  sum = ''
  opp = op
  while op !=0:
    print ('Введите операнд №', count, end = ':\t')
    a = int(input())
    count += 1
    if opp == op:
      summ = a
    else:
      summ -= a 
    sum += str (a)
    op -= 1
    if op!=0:
      sum += '-'
  print (sum, '=' , summ)
  
elif x == '*':
  summ = 1
  sum = ''
  while op !=0:
    print ('Введите операнд №', count, end = ':\t')
    a = int(input())
    count += 1
    op -= 1
    summ *= a
    sum += str (a)
    if op!=0:
      sum += '*'
  print (sum, '=' , summ)
  
elif x == '/':
  sum = ''
  opp = op
  while op !=0:
    print ('Введите операнд №', count, end = ':\t')
    a = int(input())
    count += 1
    if opp == op:
      summ = a
    else:
      summ /= a 
    sum += str (a)
    op -= 1
    if op!=0:
      sum += '/'
  print (sum, '=' , summ)
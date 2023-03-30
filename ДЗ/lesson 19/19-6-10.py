word = input('Введите строку: ')
sum = 0
symb=dict()
for i in word:
  symb[i]=word.count(i)
for i in symb:
  if symb[i]%2!=0:
    sum+=1
if sum <= 1:
  print('Можно сделать палиндромом. ')
else:
  print('Нельзя сделать палиндромом. ')
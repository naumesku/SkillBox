def delit (x):
  if x<2:
    x = int(input ('Число должно быть большe 1, попробуйте еще раз: '))
  delit = 1
  for num in range (2,x+1):
    delit = (x/num)%10
    if delit - round (int(delit), 10)==0:
      print('Наименьший делитель отличный от еденицы: ', num)
      break
x = int(input ('Введите число большe 1: '))
delit (x)
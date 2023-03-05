def office (x):
  id_sotr=[]
  while x!=0:
    id=int (input ('ID сотрудника: '))
    id_sotr.append(id)

    x-=1
  pr = int(input ('Какой ID ищем? '))
  for i in (id_sotr):
    if i == pr:
      l = 'на работе!'
      break
    else:
      l = 'нe работает!'
  return (l)

x=int(input ('Введите  количество сотрудников '))
print ('Сотрудник сегодня', office (x))
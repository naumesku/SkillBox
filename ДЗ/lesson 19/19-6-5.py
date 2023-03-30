text = 'Здесь что-то написано'
alp = dict()
alp2=dict()
for i in text:
  if i in alp:
    alp[i]+=1
  else:
    alp[i]=1
print ('Оригинальный словарь частот: ')
for i in sorted(alp):
  print (i, ':', alp[i])
for n in set(alp.values()):
    alp2[n]=[i for i in alp if alp[i] == n]
print ('Инвертированный словарь частот:')
for i in sorted(alp2):
  print (i, ':', alp2[i])


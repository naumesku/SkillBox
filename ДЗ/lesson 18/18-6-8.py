# s = input ('Введите строку: ')
s = 'aaAAbbсaaabb'
s2 = []
cnt = 1
i=0
for i in range (len(s)-1):
    if s[i]==s[i+1]:
        cnt +=1
    else:
        s2+=s[i],str(cnt)
        cnt=1
    i+=1
t=0
cnt=1
while True:
  t-=1
  if s[t]==s[t-1]:
    cnt+=1
  else:
    s2+=s[t],str(cnt)
    # s2+=str(cnt)
    break
print (''.join(s2))






# Задача 8. Сжатие
# С увеличением объема данных возникла потребность в сжатии этих данных, при этом не потеряв важную информацию.
# Для этого было придумано кодирование, которое осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на экран. Кодирование должно учитывать регистр символов.
#
# Пример:
# Введите строку: aaAAbbсaaaA
#
# Закодированная строка: a2A2b2с1a3A1

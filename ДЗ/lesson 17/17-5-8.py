import random
n = int (input('Количество палок: '))
k = int (input('Количество бросков: '))
line = ['I' for _ in range (n)]
for i in range (k):
    print ('Бросок ', i+1)
    l = random.randint(1, n)
    r = random.randint(l, n)
    print ('Сбиты палки с номера ',l , 'по номер ', r)
    line[l-1:r] = ['.' for _ in range (r-l+1)]
for i in line:
    print (i, end ='')

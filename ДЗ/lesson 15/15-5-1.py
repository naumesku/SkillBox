n = int(input('Введите целое число '))
list_2 = []
for i in range (1, n+1):
    if i%2!=0:
        list_2.append(i)
print ('Список из нечетных чисел', list_2)



list = []
sum = 0
N = int (input ('Введите колчисетво чисел: '))
for i in range (N):
    print ('Введите', i+1,'число: ', end = '')
    number = int (input())
    list.append(number)
K = int (input ('Введите делитель '))

for i_num in range (N):
    if list[i_num] % 10 == 0:
         print('Индекс числа ',list[i_num],':', i_num)
         sum += i_num
print (i)




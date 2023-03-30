n = int(input('Введите максимальное число: '))
sets = set(range(1, n + 1))
while True:
    str = input('Нужное число есть среди вот этих чисел: ').lower()
    if str == 'помогите':
        print('Артём мог загадать следующие числа: ', end = ' ')
        for i in sets:
            print (i, end ='')
        break
    else:
        answer = (input('Ответ Артема: ')).lower()
        if answer == 'да':
            sets &= set([int(i) for i in str.split()])
        else:
            sets = sets.difference(set([int(i) for i in str.split()]))



 # 1 2 3 4 5
 # 2 4 6 8 10
 # Помогите!

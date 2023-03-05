def years (a, b):
    for num in range (a,b+1):
        num1 = num
        sum1 = sum2 = 0
        x = num % 10
        y = (num//10)%10
        while num != 0:
            x1 = num % 10
            if x1 == x:
                sum1+=1
            if y == x1:
                sum2+=1
            num//=10
        if sum1==3 and sum2==3:
            print (num1)
a = int(input ('Введите первый год '))
b = int(input ('Введите второй год '))
print ('Годы от ', a, 'до', b, ' с тремя одинаковыми цифрами: ')
years (a, b)
def years (a, b):
    for num in range (a,b+1):
        sum1 = sum2 = 0
        x = num % 10
        y = (num//10)%10
        #if x == y:
         #   sum1=1
        while num != 0:
            x1 = num % 10
            print (x1)
            if x1 == x:
                sum1+=1
            print ('sum1= ',sum1)
            elif y == x1:
                sum2+=1
            print ('sum1= 'sum2)
            num//=10
            print ('num = ', num)
            print ('x1= ',x1)
        if sum1==3 and sum2==3:
            print (num)
a = int(input ('Введите первый год '))
b = int(input ('Введите второй год '))
years (a, b)
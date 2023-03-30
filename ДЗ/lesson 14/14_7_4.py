def rev (a):
    x_1 = a1 = int(a)
    count = 0
    sum=0
    sum2=0
    x_2 = round(a - int(a), 10)
    #Считаем количеств цифр в целом числе
    while x_1 !=0:
        x_1 //=10
        count += 1
    #Меняем целую часть числа
    while count !=0:
        count -= 1
        a2 = a1%10
        sum += a2*10**count
        a1 //= 10
    # Меняем дробную часть числа
    while x_2 !=0:
        count += 1
        x_2 *= 10
        sum2 += int(x_2)*10**count
        x_2 = round(x_2 - int(x_2), 10)
    return (sum + sum2/10**(count+1))
x = float (input('Введите пeрвое число '))
y= float (input('Введите второе число '))
print ('Первое число наоборот = ', rev(x))
print ('Второе число наоборот = ', rev(y))
print ('Сумма = ', rev(x)+rev (y))


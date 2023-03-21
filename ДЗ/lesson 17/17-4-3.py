import random
number = [random.randint(-100,100) for _ in range (10)]
print('Первоначальный список', number)
a = random.randint(0,5)
b = random.randint(5,10)
number[a:b]=[]
print('А =',a, 'B =', b)
print ('Итоговый список',number)




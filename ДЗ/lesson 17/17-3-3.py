import random
units_1 = [random.randint(50,80) for _ in range(10)]
units_2 = [random.randint(30,60) for _ in range(10)]

units_3 = [('Погиб' if (units_1[i]+units_2[i])>100 else 'Выжил') for i in range(10)]

print ('Урон первого отряда: ', units_1)
print ('Урон второго отряда: ', units_2)
print ('Состояние третьего отряда: ', units_3)

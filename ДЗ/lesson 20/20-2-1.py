import random
tpl_1 = tuple (random.randint(0,5)  for _ in range(10))
tpl_2 = tuple (random.randint(-5,0)  for _ in range(10))
tpl_3=tpl_1+tpl_2
tpl_3.count(0)
print ('Третий кортеж: ',tpl_3,'количество нулей: ',tpl_3.count(0))
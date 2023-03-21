import random
n = int (input('Введите количество цифр: '))
numbers = [random.randint (0,5) for _ in range (n)]
print(numbers)

numbers2 = [i for i in numbers if i!=0]
numbers3 = [i for i in numbers if i==0]
numbers2.extend(numbers3)
numbers3 = [i for i in numbers if i!=0]

print('Сжатый список: ',numbers2)
print('Cписок без нулей: ',numbers3)

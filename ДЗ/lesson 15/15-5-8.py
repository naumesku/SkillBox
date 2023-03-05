n = int (input('Кол-во элементов: '))
elements = []
new_list = []
for _ in range (n):
    element = int (input('Введите элеменет: '))
    elements.append(element)
print ('Изначальный список: ',elements)
k = int (input('Сдвиг: '))
for i in range (n):
    new_list.append(elements[(i-k)])
print ('Сдвинутый список: ',new_list)

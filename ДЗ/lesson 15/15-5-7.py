n = int (input('Кол-во контейнеров: '))
box = []
for _ in range (n):
    v = int (input('Введите вес контейнера: '))
    while v<0 or v>200:
        v = int(input('Не верный вес. Введите вес  еще раз: '))
    box.append(v)
print (box)
x = int (input('Масса нового контейнера: '))
while x < 0 or x > 200:
    x = int(input('Не верный вес. Введите вес  еще раз: '))
for index in range (n-1,-1,-1):
    # print(index)
    if box [index] < x < box [(index-1)]:
        print ('Номер, куда встанет новый контейнер: ', index+1)
        break
    elif box [index] == x:
        print ('Номер, куда встанет новый контейнер: ', index+2)
        break

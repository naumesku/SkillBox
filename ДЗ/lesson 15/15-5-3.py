N = int(input ('Введите Количество клеток '))
cell_list = []
new_list = []

for i in range (N):
    print ('Эфективность ',i+1,'клетки ', end='')
    f = int(input())
    cell_list.append(f)
for index in range (N):
    if index > cell_list[index]:
        new_list.append(cell_list[index])
print('\nНеподходящие значения: ',new_list)
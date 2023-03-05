vk_list = []
new_list = []
N = int(input('Количество видеокарт: '))
for v in range(N):
    print(v + 1, 'Видеокарта: ', end='')
    vk = int(input())
    vk_list.append(vk)
max = vk_list[0]
for i in range(N):
    if max < vk_list[i]:
        max = vk_list[i]
for ind in range(N):
    if vk_list[ind] != max:
        new_list.append(vk_list[ind])
print ('Старый список видеокарт: ', vk_list)
print ('Новый список видеокарт: ', new_list)


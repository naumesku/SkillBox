list_man = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list = []
for i in range (len(list_man)):
    if i%2==0:
        new_list.append(list_man[i+1])
print (new_list)


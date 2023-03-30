while True:
    pathern = input('Введите шаблон поздравления, в шаблоне нужно использовать конструкцию {name} и {age}: ')
    if '{name}' in pathern and '{age}' in pathern:
        break
    else:
        print ('В шаблоне нужно использовать конструкцию {name} и {age}')
name_list = input('Введите ФИ через запятую: ').split(', ')
age_man = input('Введите возраст через пробел: ').split()
for i in range (len(name_list)):
    print (pathern.format(name = name_list[i], age = age_man[i]))
mans = [' '.join([name_list[i], str(age_man[i])]) for i in range (len(name_list))]
print ('Именинники: ', ', '.join(mans))



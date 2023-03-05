films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
new_films = []
film = input('Введите название фильма: ')
while film != 'end':
    count = 0
    for i in range (len(films)):
        if films[i] == film:
            new_films.append(films[i])
        else:
            count +=1
    if count == 9:
        print('Такого фильма в базе нет')
    film = input('Введите название фильма: ')
print ('Итоговый список фильмов: ', new_films)
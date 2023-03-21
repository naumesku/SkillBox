def film_list(film, films):
    for i in films:
        if i == film:
            return True
    else:
        return False
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица']
my_films=[]
film = 0
while film != 'end':
    print('Ваш текущий топ фильмов: ', my_films)
    film = input('Введите название фильма: ')
    while film_list(film, films) == False:
        film = input('Такого фильма на сайте нет. Введите фильм еще раз: ')
    print('Команды: добавить, вставить, удалить')
    command = input('Введите команду: ')
    if command == 'добавить':
        if film_list(film,my_films) == False:
            my_films.append(film)
        else:
            print('Такой фильм уже есть в списке')
    if command == 'вставить':
        if film_list(film, my_films) == False:
            ind = int (input('Под каким номером будет фильм?: '))
            my_films.insert(ind-1,film)
        else:
            print('Такой фильм уже есть в списке')
    if command == 'удалить':
        if film_list(film, my_films) == False:
            print('Фильма и так нет в списке')
        else:
            my_films.remove(film)

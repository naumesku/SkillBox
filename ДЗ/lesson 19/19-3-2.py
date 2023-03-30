def maik (team,status,dict):
    new_list = [man['name'] for man in dict.values()
                if man['team']==team and man['status'] == status
    ]
    return new_list
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
print('Все члены команды из команды А, которые отдыхают:', maik('A','Rest',players_dict))
print('Все члены команды из группы B, которые тренируются:', maik('B','Training',players_dict))
print('Все члены команды из команды C, которые путешествуют:', maik('C','Travel',players_dict))








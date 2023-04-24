students = {
    1: {'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
        },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
lst = [(i, v)
       for i, s in students.items() for k, v in s.items() if k == 'age']
print(lst)
def f(dict):
    fullint = [x for i, s in dict.items() for k, v in s.items() if k == 'interests' for x in v]
    ln = len([d for lsnm in [v for i, s in dict.items() for k, v in s.items() if k == 'surname'] for d in lsnm])
    return fullint,ln
fullint, len = f(students)
print('Список всех интересов: ', fullint)
print('Длина всех фамилий : ', len)
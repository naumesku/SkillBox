data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
serial = int (input('Введите серию паспорта: ' ))
numb = int (input('Введите номер паспорта: ' ))

def sn(s,n):
    for k,v in data.items():
        if s in k and n in k:
            print(v[0], v[1])
    else:
        print('Таккого паспорта в базе нет.')
sn(serial,numb)
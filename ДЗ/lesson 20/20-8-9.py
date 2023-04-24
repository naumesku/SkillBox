n = int (input('Введите количество строк протокола. '))
names = []
scr=[]
sct_m =[]
nm_m=[]
for i in range(n):
    score , name = input('{} запись:'.format(i+1)).split(' ')
    if name not in names:
        scr.append(int(score))
        names.append(name)
    for i,s in enumerate(names):
        if s==name and int(scr[i])< int(score):
            scr.remove(scr[i])
            names.remove(s)
            scr.append(int(score))
            names.append(name)
for i in range(len(scr)):
    x = max(scr)
    for i,s in enumerate (scr):
        if s == x:
            sct_m.append(s)
            nm_m.append(names[i])
            names.remove(names[i])
            scr.remove(s)
sct_m.extend(scr)
nm_m.extend(names)
for i in range (3):
    print(i+1,'место.',nm_m[i], sct_m[i])
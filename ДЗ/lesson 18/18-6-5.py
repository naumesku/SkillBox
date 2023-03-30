def koor(text):
    texts = text.split()
    if texts [0] == 'South'or texts [0] == 'West ':
        return int (texts [1])*-1
    else:
        return int(texts [1])
oy = input('По оси OY: ')
ox = input('По оси OX: ')
print ('Координаты: ',koor(ox),koor(oy))


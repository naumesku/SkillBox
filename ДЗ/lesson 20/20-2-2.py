import math

def cirkl(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * (math.pi * r ** 2)
    return side, full

r = int(input('Введите радиус: '))
h = int(input('Введите высоту: '))
sid, ful = cirkl(r, h)
print('Площадь боковой поверхности: ',round(sid,2))
print('Полная площадь: ', round(ful,2))
def detect (x, y, r):
  if r<0:
    print ('Радиус не может быть отрицательным, введите еще раз')
    r = float(input ('Радиус = '))
  import math
  if math.sqrt(x**2 + y**2)<=r:
    print ('Монетка где-то рядом')
  else:
    print ('Монетки в области нет')

print ('Введите координаты монетки')
x = float(input ('X= '))
y = float(input ('Y= '))
r = float(input ('Радиус = '))
detect (x, y, r)
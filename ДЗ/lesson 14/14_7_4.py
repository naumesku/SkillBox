def count (x):
    count = 0
    while  x!= 0:
      x //=10
      count +=1
    return count
def sum (x, count):
  summ = 0
  while count !=0:
    summ += (x % 10)
    x //= 10
    count -= 1
  return summ

x = int (input ('Введите X: '))
print ('Сумма чисел: ', sum(x, count(x)))
print ('Кол-во цифр: ', count (x))
print ('Разность суммы и количества цифр: ', sum(x, count(x)) - count (x))



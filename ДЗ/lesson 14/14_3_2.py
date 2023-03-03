x = input ('Выберите операцию: ')
while x!= '+' and x!='-' and x!='*' and x!='/':
  x = input ('Ошибка: такой операции не существует. Попробуйте ещё раз.')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

if x == '+':
  print (a, x, b, ' = ', a + b)
elif x == '-':
  print (a, x, b, ' = ', a - b)
elif x == '*':
  print (a, x, b, ' = ', a * b)
elif x == '/':
  print (a, x, b, ' = ', a / b)
n=int (input ('Сколько чисел в списке? : '))
num =[]
for _ in range(n):
  x=int (input ('Введите число : '))
  num.append(x)
print ('Изначальный список: ', num)
x = True
while x == True:
  x = False
  for i in range (n-1):
    if num[i]>num[i+1]:
      num[i],num[i+1] = num[i+1],num[i]
      x = True
print('спикок по возрастанию: ', num)
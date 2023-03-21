def zero (list):
    for i in worker:
        if i == 0:
            return True
    return False
n = int(input('Кол-во сотрудников: '))
worker = []
for i in range (n):
    print('Зарплата', i+1, 'сотрудника: ', end = '')
    wages = int (input())
    worker.append(wages)
print('Начальный список зарплат: ',worker)
while zero(worker)==True:
    worker.remove(0)

print('Конечный список зарплат: ',worker)
print('Минимальная зарплатa: ',min(worker))
print('Максммальная зарплатa: ',max(worker))

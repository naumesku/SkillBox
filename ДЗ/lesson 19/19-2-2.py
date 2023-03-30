incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
sum = 0
for i in incomes:
    sum+=incomes[i]
print ('Общий доход за год составил: ', sum)
for i in incomes:
    if incomes[i] == min(incomes.values()):
        f = i
print ('Самый маленький доход у ', f ,' Он составляет', min(incomes.values()), ' рублей')
incomes.pop(f)
print ('Новый список: ', incomes)

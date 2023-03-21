prises = []
for _ in range (5):
    prise = float(input('Цена на товар: '))
    prises.append(prise)
precent = int(input ('Повышение на первый год? '))/100
print (precent)
year_1 = [x+precent*x for x in prises]
precent = int (input ('Повышение на второй год? '))/100
year_2 = [x+precent*x for x in year_1]
print ('Сумма цен за каждый год: ', round(sum(prises),2),round(sum(year_1),2), round(sum(year_2),2))

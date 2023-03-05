word = list(input ('Введите слово: '))
print (word)
sum=0
for ind in (word):
    count = 0
    for i in (word):
        if ind == i:
            count += 1
    if count == 1:
        sum +=1
print('Кол-во уникальных букв: ', sum)


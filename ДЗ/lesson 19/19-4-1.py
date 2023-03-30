punkt = {'.',',',';',':','!','?'}
text='Я! Есть. Грут?! Я, Грут и Есть.'
cnt = 0
for i in text:
    if i in punkt:
        cnt+=1
print('Количество знаков пунктуации: ', cnt)

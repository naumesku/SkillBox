word = input ('Введите слово :')
symbol=input ('Введите дополнительный символ :')
text = [x*2 for x in word]
print ('Список удвоенных символов ', text)
print ('Склейка с дополнительным символом: ', [y+symbol for y in text])
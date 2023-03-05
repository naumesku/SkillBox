word = list(input ('Введите слово: '))
list_1=[]
list_2=[]
for i in range (len(word)//2):
    list_1.append(word[i])
    list_2.append(word[-i-1])
if list_1==list_2:
    print ('Слово является палиндромом')
else:
    print ('Слово неявляется палиндромом')

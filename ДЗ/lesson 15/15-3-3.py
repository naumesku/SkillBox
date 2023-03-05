number = [0,0,0]
text =[]
for i in range (3):
    print ('Введите', i+1 , 'слово ', end = '')
    word = input ()
    text.append(word)
words = input ('Слово из текста ')
while words != 'end':
    for n in range (3):
        if words == text[n]:
            number [n]+=1
    words = input('Слово из текста ')
print ('\nПодсчет слов в тексте: ')
for p in range (3):
    print(text[p], ':', number [p])





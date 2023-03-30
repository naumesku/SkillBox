number = [0,0,0]
words = input ('Введите 3 слова: ').split()
text = input ('Введите произведение: ').split()
for i in text:
    for n in range(len(words)):
        if i == words [n]:
            number[n]+= 1
print ('\nПодсчет слов в тексте: ')
for p in range (3):
    print(words[p], ':', number [p])
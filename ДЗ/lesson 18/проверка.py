words_list = [['',0],['',0],['',0]]
for i in range (3):
    print ('Введите ',i+1 ,'слово: ', end = '')
    word = input()
    words_list[i][0]=word
text = input ('Введите произведение: ').split()
for i in text:
    for n in range(len(words_list)):
        if i == words_list [n][0]:
            words_list[n][1]+= 1
print ('\nПодсчет слов в тексте: ')
for p in range (3):
    print(words_list[p][0],':',words_list[p][1])
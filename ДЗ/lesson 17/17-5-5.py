word = 'ashertihe'
text = word[::-1]
beg = text.index('h')
end = text[::-1].index('h')
x = text[beg:-end]
print ('Начальная строка: ', word )
print ('Последовательность символов между буквами h, в противоположном порядке: ', x)

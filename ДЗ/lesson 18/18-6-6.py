def big(text):
    for i in text:
        if i.isupper():
            return True
    else:
        return False
def didgit(text):
    count = 0
    for i in text:
        if i.isdigit():
            count +=1
    return count
while True:
    passw = input('Придумайте пароль: ')
    if len(passw) > 7 and big(passw) and didgit(passw)>2:
        print ('Это надёжный пароль!')
        break
    else:
        print ('Пароль ненадёжный. Попробуйте ещё раз.!')
ppl ={} # общий словарь
step = dict() # словарь для подстета
n = int(input('Введите количество человек: '))
for i in range (n-1):
    man = input ('{} пара: '.format(i+1)).split()
    ppl[man[0]]=man[1]
    step [man[0]] = 0
    step [man[1]] = 0
for i in ppl:
    s = i
    while s in ppl:
        step[i]+=1
        s=ppl[s]
for i in sorted(step):
    print(i, step[i])
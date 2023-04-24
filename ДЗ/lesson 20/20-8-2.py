def is_prime(num):
    if num == 0 or  num == 1:
        return False
    sum = 0
    for n in range(2,num):
        if num % n==0:
            sum +=1
        if sum == 0:
            return True
        else:
            return False

def fun (text):
    answer = []
    if isinstance(text,dict):
        for i, s in enumerate([i for y, i in enumerate(text.items()) if is_prime(y)]):
            ans = dict()
            ans[s[0]] = s[1]
            answer.append(ans)
    else:
        answer = [i for y, i in enumerate(text) if is_prime(y)]
    print(answer)

text = {'name': 5, 'team': 2, 'status': 1, 'nsdame': 15, 'treeam': 12, 'stus': 20}
# text = ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
# text = 'ОДвыоыи!'
fun (text)

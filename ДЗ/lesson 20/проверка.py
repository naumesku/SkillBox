str = 'abcd'
tpl = (10, 20, 30, 40)
def zipp (a,b):
   tpla = tuple(a)
   tplb = tuple(b)
   answer = []
   for i, s in enumerate (tpla):
      ptll=(s,tplb[i])
      answer.append(ptll)
   return (tuple(answer))
print(zipp(str,tpl))
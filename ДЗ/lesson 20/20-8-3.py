text = (0,1,2,3,4,5,2,6,7)
n=9
def fun (tx, n):
  if n not in tx:
      answer=()
  elif tx.count(n)==1:
      indx = [i for i, s in enumerate(tx) if s == n]
      answer = list(tx)[indx[0]:]
  else:
      indx = [i for i, s in enumerate(tx) if s == n]
      answer = list(tx)[indx[0]:indx[1]+1]
  return tuple(answer)
print (fun(text,n))
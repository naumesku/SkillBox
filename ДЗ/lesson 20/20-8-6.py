lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print ([(lst[i-1],lst[i]) for i,s in enumerate(lst) if i%2 != 0])

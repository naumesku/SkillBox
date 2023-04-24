def srt (data):
    for i,s in enumerate(data):
        if int(s) != s:
            return data
    else:
        return sorted(list(data))
dct = (0, 1, 7, 3, 8, 2,9, 4, 5, 10, 6, 7)
print (srt (dct))

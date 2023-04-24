str = 'О Дивный Новый мир!'
dct = {         "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            }
def fun (txt):
    if isinstance (txt,dict):
        lsts = [v for i,v in enumerate(txt) if i%2 == 0]
        answ=[]
        for x in lsts:
            ans = dict()
            ans[x] = txt[x]
            answ.append(ans)
    else:
        answ = [v for i,v in enumerate(txt) if i%2 == 0]
    return answ
print (fun(dct))




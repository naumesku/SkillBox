import random
def kv(lst):
    dct = dict()
    for k, v in enumerate(tuple(lst)):
        dct[k] = v
    return dct

alph='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
lits1 = [alph[random.randint(0,33)] for _ in range (10)]
lits2 = [alph[random.randint(0,33)] for _ in range (10)]

print('Первый список: ', kv(lits1))
print('Второй список: ', kv(lits2))

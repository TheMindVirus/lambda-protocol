#psk = "portal mad c bool"
#lnk = [5, 4, 7, 13, 9, 8, 6, 0, 2, 1, 3, 14, 11, 15, 16]

psk = "portal b mad cool"
lnk = [5, 4, 9, 7, 11, 10, 6, 0, 2, 1, 3, 14, 13, 15, 16]

def decypher(psk):
    return lambda x: [psk[i] for i in x]

gen = decypher(psk)
obj = gen(lnk)
txt = ''.join(obj)
print(txt)

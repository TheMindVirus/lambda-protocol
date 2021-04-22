#TEXT = "portal b mad cool"
TEXT = "portal mad c bool"
TEST = False

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
B = A.copy()
#C = [5, 4, 9, 7, 11, 10, 6, 0, 2, 1, 3, 14, 13, 15, 16, 8, 12]
C = [5, 4, 7, 13, 9, 8, 6, 0, 2, 1, 3, 14, 11, 15, 16, 10, 12]

def decypher(psk):
    return lambda x: [psk[i] for i in x]

if (TEST):
    print(B)
    for i in range(0, len(A)):
        idx = B.index(C[i])
        print(i, idx, B[i], B[idx])
        tmp = B[i]
        B[i] = B[idx]
        B[idx] = tmp
        print(B)
else:
    import time

    print(TEXT)
    
    for i in range(0, len(A)):
        time.sleep(0.2)
        idx = B.index(C[i])
        tmp = B[i]
        B[i] = B[idx]
        B[idx] = tmp
        gen = decypher(TEXT)
        obj = gen(B)
        txt = ''.join(obj)
        print(txt)

    tmp = A
    A = C
    C = tmp

    for i in range(0, len(A)):
        time.sleep(0.2)
        idx = B.index(C[i])
        tmp = B[i]
        B[i] = B[idx]
        B[idx] = tmp
        gen = decypher(TEXT)
        obj = gen(B)
        txt = ''.join(obj)
        print(txt)
    

def fibb(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
        
    return a


n = 1
while fibb(n+1) / fibb(n) != fibb(n+2) / fibb(n+1):
    n += 1
else:
    print(n)
    print(fibb(n+1) / fibb(n))

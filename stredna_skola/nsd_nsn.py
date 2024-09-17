def nsd(m, n):
    if m > n:
        min = n
    else:
        min = m

    result = 1
    for i in range(1, min+1):
        if m % i == 0 and n % i == 0:
             result = i 
    return result

def nsd(m, n):
    while n:
        m, n = n, m % n
    return m

def nsn(m, n):
    nasobok = (m * n) / nsd(m, n)
    return nasobok

lst = [20, 30]
print(nsd(*lst))
print(nsn(*lst))
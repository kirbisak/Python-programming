def faktorial(n, k):
    kf = 1
    nf = 1
    nkf = 1
    if 0 <= k <= n:
        for i in range(1, n+1):
            nf = nf * i
        for i in range(1, k+1):
            kf = kf *i
        for i in range(1, (n-k)+1):
            nkf = nkf * i
        komb_cislo = nf / (kf * nkf)
        print(komb_cislo)
    else:
        print("nemozno")
faktorial(6, 2)

def comb_num(n):
    if n == 1:
        return 1
    return n * comb_num(n-1)

print(comb_num(5))
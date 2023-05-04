def fibb(n):
    if n <= 0:
        return None
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(1, n + 1):
            c = a + b
            a = b
            b = c
        zlaty_rez = b / a
        return zlaty_rez


n = int(input("Zadaj pocet clenov fibb postupnosti: "))
if fibb(n) != None:
    print(f"Hodnota zlateho rezu z {n} clenov, je priblizne: {fibb(n)}")
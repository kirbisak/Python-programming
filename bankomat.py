def bankomat(n):
    listBank = [500, 100, 50, 20, 10]
    for i in range(len(listBank)):
        if int(n) // listBank[i] != 0:
            temp = int(n) // listBank[i]
            print(f"vydam ti {listBank[i]} {temp} krat")
            n = int(n) - listBank[i] * temp

bankomat("850")